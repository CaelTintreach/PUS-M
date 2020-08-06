from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, NumberRange
from application.models import Projects 

class ProjectForm(FlaskForm):
	projectName = StringField('Project Name',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )
	projectComplete = BooleanField('Completed?')
	submit = SubmitField('Add Project')

class UpdateProjectForm(FlaskForm):
    projectName = StringField('Project Name',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )
    projectComplete = BooleanField('Completed?')
    submit = SubmitField('Add Project')