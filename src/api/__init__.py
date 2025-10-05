from flask import Flask
from flask_cors import CORS
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI="sqlite:///app.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    db.init_app(app)

    # Registra blueprint
    from .routes import api as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    # Crea tablas en dev
    @app.before_first_request
    def create_tables():
        db.create_all()

    return app