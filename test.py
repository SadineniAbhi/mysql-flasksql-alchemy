from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/bookstore'
    db.init_app(app)
    return app

app = create_app()

with app.app_context():
    store1 = StoreModel(name="Store 1")
    store2 = StoreModel(name="Store 2")
    store3 = StoreModel(name="Store 3")

    # Add instances to the session
    db.session.add(store1)
    db.session.add(store2)
    db.session.add(store3)

    # Commit the changes to the database
    db.session.commit()
