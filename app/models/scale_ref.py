from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from app.models import db

class ScaleRef(db.Model):
    """
    Scale Reference table model
    """
    __bind_key__ = 'scale_ref'
    # override default table name
    __tablename__ = 'scale_ref'

    scale_name = db.Column(db.String(255))
    unscaled = db.Column(db.String(255))
    scaled = db.Column(db.String(255), primary_key=True)

    def __init__(self):
      """Constructor."""