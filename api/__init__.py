from flask import Flask
from .config import DevelopmentConfig, TestingConfig, ProductionConfig
from flask_marshmallow import Marshmallow
from .database.database import engine, Base
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    app = Flask(__name__, instance_relative_config=True, template_folder='swagger/templates')
    app.config.from_object(DevelopmentConfig)
    Base.metadata.create_all(engine)

    from .routes import bp_routes
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "my list of users"
        }   
    )
    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix= SWAGGER_URL)
    app.register_blueprint(bp_routes, url_prefix='/')
    return app


app = create_app()
ma = Marshmallow(app)

