from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


#criar classe

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f'{self.name} - {self.description}'

@app.route('/')
def index():
    return 'Hello'

#fazer um GET request

@app.route('/drinks')
def get_drinks():

    return {"drinks": "drink data"} #está funcionando, porém temos que conectar com uma base de dados