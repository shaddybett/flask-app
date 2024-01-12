from flask import Flask,render_template
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
    pets_list = Pet.qury.all()
    return render_template('about.html', pets = pets_list)

@app.route('/owners')
def owners():
    owners_list = Owner.query.all()
    return render_template('owners.html', owners = owners_list)

__name__=='__main__'
app.run(debug=True) 

