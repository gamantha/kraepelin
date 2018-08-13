from app.models import db

class Kraepelin(db.Model):
    """
    Kraepelin table model
    """

    # override default table name
    __tablename__ = 'kraepelins'

    id = db.Column(db.Integer, primary_key=true)
    answers = db.Column(db.Text)
