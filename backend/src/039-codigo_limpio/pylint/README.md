### Pylint 

#### [Referencia](https://pylint.readthedocs.io/en/latest/)

Pylint sirve para mantener una sintaxis limpia en Python acorde con los estándares.

### Instalación
```
git clone https://github.com/PyCQA/pylint.git
cd pylint & python3 setup.py install
```

### Configuración
Ejecutamos `pylint --generate-rcfile > .pylintrc` y configuramos el archivo que aparecerá en la carpeta ([aquí está la lista de posibles opciones](https://pylint.readthedocs.io/en/latest/technical_reference/features.html)).

### Ejecución
Para ejecutarlo simplemente `pylint <carpeta_a_analizar>` y todo el código será testeado por pylint en busca de malas prácticas. Si estamos en un entorno virtual lo podemos ejecutar así: 
```
<nombre_del_entorno>/bin/pylint <carpeta_a_analizar>
```

