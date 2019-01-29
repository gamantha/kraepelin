from app.models import db
from sqlalchemy.orm import relationship

class Quota(db.Model):
    """
    Quota table model
    """
    # override default table name
    __tablename__ = 'quota'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    quota = db.Column(db.Integer)

    def __init__(self):
      """Constructor."""
