from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db,Pet,Owner


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()
@app.route('/')
def home():
    return '<h1>Welcome Home!</h1>'

@app.route('/about')
def about():
    return 

