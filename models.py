from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(60))
    productDesc = db.Column(db.String(120))
    isStock = db.Column(db.Boolean, default=True)
    stockCount = db.Column(db.Integer, default=0)
    productImg = db.Column(db.String(255))
