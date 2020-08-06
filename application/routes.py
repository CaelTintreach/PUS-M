from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Projects 
from application.forms import ProjectForm, UpdateProjectForm

@app.route('/addproject', methods=['GET', 'POST'])
def addproject():
	form = ProjectForm()
	if form.validate_on_submit():
		project = Projects(
			projectName=form.projectName.data,
			projectComplete=form.projectComplete.data
			)
		db.session.add(project)
		db.session.commit()
		return redirect(url_for('home'))
	else:
		print(form.errors)
	return render_template('addproject.html', title='Add Project', form=form)

@app.route('/')
@app.route('/home') #The homepage will display all projects currently in the database as well as their status. 
def home():
    projectData = Projects.query.all()
    return render_template('home.html', title='home', posts=projectData)

@app.route('/updateproject/<project_id>', methods=['GET', 'POST'])
def updateproject(project_id):
	project = Projects.query.filter_by(project_id = id).first()
	form = UpdateProjectForm()
	if form.validate_on_submit():
		project.projectName = form.projectName.data
		project.projectComplete = form.projectComplete.data
		db.session.commit()
		return redirect(url_for('home', project_id = id))
	elif request.method == 'GET':
		form.projectName.data = project.projectName
		form.projectComplete.data = project.projectComplete
	return render_template('updateproject.html', title='Update Project', form = form)

