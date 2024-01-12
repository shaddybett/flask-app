from flask import Flask
from models import Pet,db,Owner
from app import app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///best.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    pet_data = {
        'name': 'Jojo',
        'owner_id': 1
    }

    owner_data = {
        'name': 'Sway'
    }

with app.app_context():
    new_pet = Pet(**pet_data)
    new_owner = Owner(**owner_data)
with db.session.begin():
    db.session.add(new_pet)
    db.session.add(new_owner)
    db.session.commit()                                                           