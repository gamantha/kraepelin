import logging
import bcrypt
from app.models import db
from app.models.user import User
from app.models.quota import Quota

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

  def login_email(self, email, password):
    """
    Login user by their email
    """
    try:
      user = db.session.query(User).filter_by(email=email).first()
      data = {}
      data = user.__dict__ if user else None
      if (bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))):
        logger.info('password match, fetching quota data.')
        quota = db.session.query(Quota).filter_by(user_id=user.user_id).first()
        if quota is None:
          raise Exception('no quota')
        data['quota'] = quota.quota
        return data
      else: 
        logger.warning('password does not match')
        return None
    except Exception as e:
      logger.warning('an error occured when reading database: %s', e)
      raise e
