# archivo temporal que debe ser eliminado
from app import create_app

app = create_app()

print("Base en uso:", app.config["SQLALCHEMY_DATABASE_URI"])


