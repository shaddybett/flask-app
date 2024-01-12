from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    __tablename__='pets'
    name = db.Column(db.String(200),nullable=False)
    age = db.Column(db.Integer)
    Owner = db.column(db.String(200))

class Owner(db.Model):
    __tablename__='owners'
    name = db.Column(db.String(200),nullable=False)
    age = db.Column(db.Integer)
    pet = db.Column(db.String(200))