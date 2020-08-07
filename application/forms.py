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
    submit = SubmitField('Add Project')

class UserStoriesForm(FlaskForm):
    userstoryName = StringField('User Story Name',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )

    userstoryDesc = StringField('User Story Desc',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )

    userstoryProject = IntegerField('Input Numeric ID Of Project',
            validators = [
                DataRequired(),
            ]
    )
    submit = SubmitField('Add User Story')

class UpdateUserStoriesForm(FlaskForm):
    userstoryName = StringField('User Story Name',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )

    userstoryDesc = StringField('User Story Name',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )

    userstoryProject = IntegerField('Input Numeric ID Of Project',
            validators = [
                DataRequired(),
            ]
    )

    userstoryComplete = BooleanField('Completed?')
    submit = SubmitField('Add User Story')