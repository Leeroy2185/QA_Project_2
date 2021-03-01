from application import db
from application.models import Creature

db.drop_all()
db.create_all()