from application import db

class Projects(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	projectName = db.Column(db.String(100), nullable=False, unique=True)
	projectComplete = db.Column(db.Boolean, nullable=False, unique=False, default=False)

	def __repr__(self):
		return ''.join([
			'Project ID: ', self.id, '\r\n',
			'Project Name: ', self.projectName, '\r\n'
		])