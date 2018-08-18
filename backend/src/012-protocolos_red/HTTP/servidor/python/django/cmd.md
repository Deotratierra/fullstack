## Comandos en Django

- Comenzar un nuevo proyecto: `django-admin startproject <nombre-proyecto>`. Creará la siguiente estructura:

    <nombre-proyecto>/
        manage.py
        <nombre-proyecto>/
            __init__.py
            settings.py
            urls.py
            wsgi.py

- Comenzar una nueva aplicación dentro del proyecto: `python manage.py startapp <nombre-aplicación>`. Creará la siguiente estructura:

    <nombre-aplicación>/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py

- Crear un nuevo superusuario: `python3 manage.py createsuperuser`
- Correr el servidor: `python manage.py runserver`
- Aplicar migraciones: `python manage.py makemigrations && python manage.py migrate`

> Da lo mismo usar `django-admin` que `python manage.py`.
