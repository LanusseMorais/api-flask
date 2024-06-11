from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from config import Config

db = SQLAlchemy()
migrate = Migrate()
swagger = Swagger()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    swagger.init_app(app)

    from app import routes
    app.register_blueprint(routes.bp, url_prefix='/api/v1')

    return app
