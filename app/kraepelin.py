import logging
import logging.config
import os

from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from .routes.public import public_routes

from .config import settings

logging.config.dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'formatter': 'default'
    }},
    'root': {
        'level': os.getenv('LOGGING_LEVEL_ROOT', 'INFO'),
        'handlers': ['wsgi']
    }
})


def create_app(configuration):
    log = logging.getLogger(__name__)
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    # logging_tree.printout()
    log.info('Starting Flask app %s...', __name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    # set configuration
    app.config.from_object(configuration)
    # register blueprint
    app.register_blueprint(public_routes)
    return app

app = create_app(settings)

if __name__ == "__main__":
    app.run()