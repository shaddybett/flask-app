from models import Pet,db,Owner
from app import app
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

    db.session.add(new_pet)
    db.session.add(new_owner)
    db.session.commit()                                                           