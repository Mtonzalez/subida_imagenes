# Usar una imagen base de Python 3.9 (compatible con Raspberry Pi)
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema antes de instalar paquetes Python
RUN apt update && apt install -y libpq-dev gcc

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .
# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5000 para Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "run.py"]