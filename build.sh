# exit on error
set -o errexit

# Instalar librerías
pip install -r requirements.txt

# Juntar archivos estáticos (CSS, JS, Img)
python manage.py collectstatic --no-input

# Correr migraciones en la base de datos de la nube
python manage.py migrate