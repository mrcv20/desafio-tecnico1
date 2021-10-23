from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import DevelopmentConfig, TestingConfig, ProductionConfig
from os import getenv
from flask_marshmallow import Marshmallow

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DevelopmentConfig)

    if getenv('FLASK_ENV') in ['testing']:
        app.config.from_object(TestingConfig)
    if getenv('FLASK_ENV') in ['production']:
        app.config.from_object(ProductionConfig)

    
    from .auth import bp_auth
    from .routes import bp_routes

    app.register_blueprint(bp_auth, url_prefix='/auth')
    app.register_blueprint(bp_routes, url_prefix='/')
    
    db.init_app(app)
    with app.app_context():
        db.create_all()
        return app

app = create_app()
ma = Marshmallow(app)