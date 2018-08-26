from datetime import datetime, timedelta
from app.models import db

class User(db.Model):
    """
    User table model
    """

    # override default table name
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self):
        self.created_at = datetime.now() + timedelta(hours=7)
        self.updated_at = datetime.now() + timedelta(hours=7)
