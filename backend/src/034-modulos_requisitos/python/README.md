### requirements.txt

- Instalar módulos: `pip3 install -r requirements.txt`
- Volcar las bibliotecas de tu proyecto: `pip3 freeze > requirements.txt`

- Instalar directamente desde un repositorio de Github (añadir al archivo):
```pip install https://github.com/<usuario>/<repositorio>/archive/<branch>.zip```
- Instalar un repositorio privado (añadir al archivo):
```git+https://<usuario>:<contraseña>@github.com/<usuario>/<repositorio>.git```

>Declaramos las versiones de los repositorios usando los mismos operadores de comparación que en python: ==, >=, <=