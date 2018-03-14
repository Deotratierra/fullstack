## `requirements.txt`
Las dependencias de un programa en Python se suelen listar en ficheros `requirements.txt` (o `dev-requirements.txt` si son necesarias para el desarrollo, realmente podemos llamar al archivo como queramos).

- Instalar módulos: `pip3 install -r requirements.txt`
- Volcar todas las bibliotecas de tu entorno: `pip3 freeze > requirements.txt`

### Manipulando las dependencias
- Declaramos las versiones de los repositorios usando los mismos operadores de comparación que en python: `==`, `>=`, `<=`.
- Podemos añadir un repositorio directamente especificando su dirección de Github mediante un link construido según la estructura: `git+https://github.com/<user>/<repo>.git`. Este link simplemente lo añadimos al archivo `requirements.txt`.
- Para añadir repositorios privados, añadimos el link según la estructura: `git+ssh://git@github.com/<user>/<repo>.git`.
