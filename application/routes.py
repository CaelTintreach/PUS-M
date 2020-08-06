from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Projects, UserStories
from application.forms import ProjectForm, UpdateProjectForm, UserStoriesForm, UpdateUserStoriesForm

@app.route('/addproject', methods=['GET', 'POST'])
def addproject():
	form = ProjectForm()
	if form.validate_on_submit():
		projectData = Projects(
			projectName=form.projectName.data,
			projectComplete=form.projectComplete.data
			)
		db.session.add(projectData)
		db.session.commit()
		return redirect(url_for('home'))
	else:
		print(form.errors)
	return render_template('addproject.html', title='Add Project', form=form)

@app.route('/adduserstory', methods=['GET', 'POST'])
def adduserstory():
	form = UserStoriesForm()
	if form.validate_on_submit():
		userstoryData = UserStories(
			userstoryName=form.userstoryName.data,
			userstoryDesc=form.userstoryDesc.data,
			userstoryComplete=form.userstoryComplete.data
			)
		db.session.add(userstoryData)
		db.session.commit()
		return redirect(url_for('home'))
	else:
		print(form.errors)
	return render_template('adduserstory.html', title='Add User Story', form=form)

@app.route('/')
@app.route('/home') #The homepage will display all projects currently in the database as well as their status. 
def home():
	return render_template('home.html', title='Home Page')

@app.route('/viewprojects')
def viewprojects():
    projectData = Projects.query.all()
    return render_template('viewprojects.html', title='View Projects', posts=projectData)

@app.route('/viewuserstories')
def viewuserstories():
    userstoryData = UserStories.query.all()
    return render_template('viewuserstories.html', title='View User Story', posts=userstoryData)

@app.route('/updateuserstory/<id>', methods=['GET', 'POST'])
def updateuserstory(id):
	updateitem = UserStories.query.filter_by(id = id).first()
	form = UpdateUserStoriesForm()
	if form.validate_on_submit():
		updateitem.userstoryName = form.userstoryName.data
		updateitem.userstoryDesc = form.userstoryDesc.data
		updateitem.userstoryComplete = form.userstoryComplete.data
		db.session.commit()
		return redirect(url_for('home', id = id))
	elif request.method == 'GET':
		form.userstoryName.data = updateitem.userstoryName
		form.userstoryDesc.data = updateitem.userstoryDesc
		form.userstoryComplete.data = updateitem.userstoryComplete
	return render_template('updateuserstory.html', title='Update User Story', form = form)

@app.route('/updateproject/<id>', methods=['GET', 'POST'])
def updateproject(id):
	updateitem = Projects.query.filter_by(id = id).first()
	form = UpdateProjectForm()
	if form.validate_on_submit():
		updateitem.projectName = form.projectName.data
		updateitem.projectComplete = form.projectComplete.data
		db.session.commit()
		return redirect(url_for('home', id = id))
	elif request.method == 'GET':
		form.projectName.data = updateitem.projectName
		form.projectComplete.data = updateitem.projectComplete
	return render_template('updateproject.html', title='Update Project', form = form)

@app.route('/deleteproject/<id>', methods=['GET', 'POST'])
def deleteproject(id):
	deleteitem = Projects.query.filter_by(id = id).first()
	db.session.delete(deleteitem)
	db.session.commit()
	return redirect(url_for('home'))

@app.route('/deleteuserstory/<id>', methods=['GET', 'POST'])
def deleteuserstory(id):
	deleteitem = UserStories.query.filter_by(id = id).first()
	db.session.delete(deleteitem)
	db.session.commit()
	return redirect(url_for('home'))