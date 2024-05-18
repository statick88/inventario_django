from .settings import *

# Configuraciones adicionales para el entorno de prueba
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
