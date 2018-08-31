from datetime import datetime, timedelta
from app.models import db

class Config(db.Model):
    """
    Config table model
    """

    # override default table name
    __tablename__ = 'config'

    id = db.Column(db.Integer, primary_key=True)
    column = db.Column(db.Integer)
    row = db.Column(db.Integer)
