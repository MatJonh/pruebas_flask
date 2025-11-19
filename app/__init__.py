from flask import Flask
from .extensions import db, migrate
from .routes.users import users_bp
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar base de datos
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar blueprints
    app.register_blueprint(users_bp, url_prefix="/api/users")

    # Ruta principal
    @app.route("/")
    def home():
        return "App Flask funcionando correctamente 🎉"

    return app
