from application import db
from application.models import Projects, UserStories

db.drop_all()
db.create_all()