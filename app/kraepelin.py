import logging
import logging.config
import os

from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from .routes.public import public_routes

from .config import settings
from .models import db

def create_app(configuration):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(configuration)
    # init db
    db.init_app(app)
    # logging_tree.printout()
    app.logger.info('Starting Flask app %s...', __name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    # register blueprint
    app.register_blueprint(public_routes)
    return app

app = create_app(settings)

if __name__ == "__main__":
    app.run()