from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    __tablename__='pets'
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(100),nullable=False)
    owner_id = db.Column(db.Integer,db.ForeignKey('owner.id'), nullable = False)
    owner = db.relationship('Owner',backref='pets')

class Owner(db.Model):
    __tablename__='owners'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
