import datetime
from models.base import Base
from db.db import db

class Token(Base):

    __tablename__ = 'Token'
    
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String())
    expiring = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id', ondelete='CASCADE'),nullable=False)

    user = db.relationship('User', backref='token', lazy=True)


    def __init__(self, token, user_id):
        self.token = token
        self.expiring = datetime.datetime.now() + datetime.timedelta(days=1)
        self.user_id = user_id