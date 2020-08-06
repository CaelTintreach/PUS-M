from application import db

class Projects(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	projectName = db.Column(db.String(100), nullable=False, unique=True)
	userstoryLink = db.relationship('UserStories', backref='ident', lazy=True)

	def __repr__(self):
		return ''.join([
			'Project ID: ', self.id, '\r\n',
			'Project Name: ', self.projectName, '\r\n'
		])

class UserStories(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	userstoryName = db.Column(db.String(100), nullable=False, unique=True)
	userstoryDesc = db.Column(db.String(100), nullable=False, unique=True)
	projectident = db.Column(db.Integer,db.ForeignKey('projects.id'), nullable = False)