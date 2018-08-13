# settings.py
import os
from dotenv import load_dotenv

load_dotenv('.env')

DEBUG = os.environ.get('DEBUG')

# SQLAlchemy and Flask-migrate configuration
SQLALCHEMY_DATABASE_URI='mysql://' + os.environ.get('DB_USER') + ':' + os.environ.get('DB_PASSWORD') + '@' + os.environ.get('DB_HOST') + '/' + os.environ.get('DB_NAME')
