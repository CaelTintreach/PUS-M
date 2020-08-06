from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, NumberRange
from application.models import Projects, UserStories

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

class UserStoriesForm(FlaskForm):
    userstoryName = StringField('Project Name',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )

    userstoryDesc = StringField('Project Name',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )

    userstoryComplete = BooleanField('Completed?')
    submit = SubmitField('Add User Story')

class UpdateUserStoriesForm(FlaskForm):
    userstoryName = StringField('Project Name',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )

    userstoryDesc = StringField('Project Name',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )

    userstoryComplete = BooleanField('Completed?')
    submit = SubmitField('Add User Story')