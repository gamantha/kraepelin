import logging
from app.models import db
from app.models.user import User
logger = logging.getLogger(__name__)

class UserService():
    """
    User service
    """ 

    def get_user_by_email(self, email):
        """
        Get user by their email
        """
        try:
            user = db.session.query(User).filter_by(email=email).first()
            data = {}
            data = user.__dict__ if user else None
            return data
        except Exception as e:
            logger.warning('an error occured when reading database: %s', e)
            raise e
