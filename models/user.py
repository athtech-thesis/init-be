from models.base import Base
from db.db import db

class User(Base):

    __tablename__ = 'User'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    surname=db.Column(db.String(25))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String())
    is_verified = db.Column(db.Boolean(), default=True)

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
