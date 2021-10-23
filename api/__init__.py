from flask import Flask
from .config import DevelopmentConfig, TestingConfig, ProductionConfig
from os import getenv
from flask_marshmallow import Marshmallow
from .database.database import engine, Base

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DevelopmentConfig)

    if getenv('FLASK_ENV') in ['testing']:
        app.config.from_object(TestingConfig)
    if getenv('FLASK_ENV') in ['production']:
        app.config.from_object(ProductionConfig)

    from .routes import bp_routes
    Base.metadata.create_all(engine)
    
    app.register_blueprint(bp_routes, url_prefix='/')
    return app


app = create_app()
ma = Marshmallow(app)