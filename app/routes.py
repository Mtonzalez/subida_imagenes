from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import ImageUploadForm
import os

# Crear un Blueprint para las rutas principales
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Obtener la ruta absoluta de la carpeta static/images
    image_folder = os.path.join(main_bp.root_path, 'static', 'images')
    
    # Listar las imágenes en la carpeta
    images = os.listdir(image_folder)
    return render_template('index.html', images=images)

@main_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    form = ImageUploadForm()
    if form.validate_on_submit():
        file = form.file.data
        
        # Obtener la ruta absoluta de la carpeta static/images
        upload_folder = os.path.join(main_bp.root_path, 'static', 'images')
        
        # Guardar el archivo en la carpeta de subida
        file.save(os.path.join(upload_folder, file.filename))
        flash('Imagen subida con éxito', 'success')
        return redirect(url_for('main.index'))
    return render_template('upload.html', form=form)