# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.models_def import db  # Use apenas o db importado

def create_app():
    """Cria e configura uma instância da aplicação Flask."""
    app = Flask(__name__, template_folder="templates", static_folder="static")

    # Configurações do aplicativo
    app.config["SECRET_KEY"] = "your_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///frota.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inicializa extensões
    db.init_app(app)
    migrate = Migrate(app, db)

    # Registra blueprints e cria tabelas
    with app.app_context():
        from .routes import car_bp
        app.register_blueprint(car_bp)
        db.create_all()

    return app