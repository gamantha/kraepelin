# settings.py
import os
from dotenv import load_dotenv

load_dotenv('.env')

DEBUG = os.environ.get('DEBUG')

SECRET_KEY=os.environ.get('SESSION_SECRET')

# SQLAlchemy and Flask-migrate configuration
SQLALCHEMY_DATABASE_URI='mysql://' + os.environ.get('DB_USER') + ':' + os.environ.get('DB_PASSWORD') + '@' + os.environ.get('DB_HOST') + '/' + os.environ.get('DB_NAME')
SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_BINDS = {
  'user': 'mysql://' + os.environ.get('DB_USER') + ':' + os.environ.get('DB_PASSWORD') + '@' + os.environ.get('DB_HOST') + '/' + os.environ.get('DB_CHAMILO'),
}