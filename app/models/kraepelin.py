from datetime import datetime, timedelta
from app.models import db

class Kraepelin(db.Model):
    """
    Kraepelin table model
    """

    # override default table name
    __tablename__ = 'kraepelins'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255))
    answers = db.Column(db.Text)
    questions = db.Column(db.Text)
    correct_count = db.Column(db.Text)
    incorrect_count = db.Column(db.Text)
    answer_count = db.Column(db.Integer)
    minute_count = db.Column(db.Text)
    filled_count = db.Column(db.Text)
    unfilled_count = db.Column(db.Text)
    starttime = db.Column(db.DateTime)
    endtime = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self):
        self.created_at = datetime.now() + timedelta(hours=7)
        self.updated_at = datetime.now() + timedelta(hours=7)
