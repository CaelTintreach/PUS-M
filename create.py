from application import db
from application.models import Projects

db.drop_all()
db.create_all()