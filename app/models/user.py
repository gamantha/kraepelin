import os
from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from app.models import db

class User(db.Model):
    """
    User table model
    """
    __bind_key__ = 'user'
    __table_args__ = {'schema': os.environ.get('DB_CHAMILO')}
    # override default table name
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    salt = db.Column(db.String(255))
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self):
        self.created_at = datetime.now() + timedelta(hours=7)
        self.updated_at = datetime.now() + timedelta(hours=7)
