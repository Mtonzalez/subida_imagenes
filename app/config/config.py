import os
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '../.env'))  # Cargar variables de entorno desde .env

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "clave_secreta")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
    ALLOWED_EXTENSIONS = set(os.getenv("ALLOWED_IMG_EXTENSIONS", "png,jpg,jpeg,gif").split(","))
