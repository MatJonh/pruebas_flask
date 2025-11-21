from flask import Flask
from .config import Config
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar base de datos y migraciones
    db.init_app(app)
    migrate.init_app(app, db)

    # Importar modelos para que SQLAlchemy los registre
    from .models import User

    # Registrar Blueprints
    from .routes import users_bp
    app.register_blueprint(users_bp)

    @app.route("/")
    def home():
        return "App Flask funcionando correctamente 🎉"

    return app

