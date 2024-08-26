from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from config import Config

# Initialize extensions (without binding to the app yet)
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with the app
    db.init_app(app)
    jwt.init_app(app)

    # Import and register blueprints inside the create_app function
    from routes.auth import auth_bp
    from routes.tasks import tasks_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(tasks_bp, url_prefix='/tasks')

    # Swagger setup
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
