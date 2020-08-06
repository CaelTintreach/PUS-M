from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Projects 
from application.forms import ProjectForm, UpdateProjectForm

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

@app.route('/')
@app.route('/home') #The homepage will display all projects currently in the database as well as their status. 
def home():
	return render_template('home.html', title='Home Page')

@app.route('/viewprojects')
def viewprojects():
    projectData = Projects.query.all()
    return render_template('viewprojects.html', title='View Projects', posts=projectData)

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

