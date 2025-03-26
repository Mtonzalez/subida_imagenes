from flask import Flask
from app.config import Config
from app.models import db
from flask_migrate import Migrate

migrate = Migrate()

# Crear una función factory para la aplicación
def create_app():
    app = Flask(__name__, template_folder='./templates')
    app.config.from_object(Config)
    
    # Inicializar la base de datos
    db.init_app(app)
    migrate.init_app(app, db)

    # Crear la carpeta de almacenamiento si no existe
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])
    
    # Importar y registrar las rutas
    from app.routes.upload import upload_bp
    app.register_blueprint(upload_bp, url_prefix="/upload")
    
    return app