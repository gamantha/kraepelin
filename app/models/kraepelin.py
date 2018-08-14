from datetime import datetime, timedelta
from app.models import db

class Kraepelin(db.Model):
    """
    Kraepelin table model
    """

    # override default table name
    __tablename__ = 'kraepelins'

    id = db.Column(db.Integer, primary_key=True)
    answers = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self):
        self.created_at = datetime.now() + timedelta(hours=7)
        self.updated_at = datetime.now() + timedelta(hours=7)
