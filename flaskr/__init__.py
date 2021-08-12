from importlib import import_module

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint

blueprint = Blueprint('base_blueprint',
                      __name__,
                      template_folder='templates',
                      static_folder='static')

db = SQLAlchemy()
login_manager = LoginManager()


def configure_database(app):
    @app.before_first_request
    def init_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    module = import_module('flaskr.routes')
    app.register_blueprint(module.blueprint)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    register_blueprints(app)
    register_extensions(app)
    configure_database(app)

    return app
