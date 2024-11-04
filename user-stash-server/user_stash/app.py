from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from user_stash.routes import routes_bp
from user_stash.extensions import db
from user_stash.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)

    # Init extensions
    db.init_app(app)

    # Migrate
    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    # Register bps
    app.register_blueprint(routes_bp, url_prefix='/api')
    return app


def run():
    app = create_app(Config)
    app.run("0.0.0.0", 5000)
