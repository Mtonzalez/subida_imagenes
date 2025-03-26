from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired

class ImageUploadForm(FlaskForm):
    file = FileField('Selecciona una imagen', validators=[DataRequired()])
    submit = SubmitField('Subir')