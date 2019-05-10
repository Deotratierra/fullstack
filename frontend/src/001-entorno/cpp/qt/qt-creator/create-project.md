## Crear un proyecto en Qt Creator

1. Abrimos Qt Creator.
2. Vamos a ``Projects`` -> ``New project`` -> ``Other project`` -> ``Empty qmake project``.
3. Indicamos el nombre del proyecto (será el nombre de la carpeta que lo envolverá) y donde irá ubicada la carpeta del proyecto.
4. Avanzamos por los pasos dejando la configuración restante por defecto.

### El sistema de construcción de Qt Creator
Este programa utiliza ``qmake`` para administrar el proceso de compilación del código. Los archivos con extensiones ``.pro`` sirven para indicarle a ``qmake`` cómo debe generar el archivo ``Makefile`` que usará para construir el proyecto.

### Configuración básica
Al crear el proyecto, veremos dentro un archivo con el nombre de nuestro proyecto y extensión ``.pro``. Debemos añadirle dentro lo siguiente:

```
TEMPLATE = app
TARGET = name_of_the_app

QT = core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets
```

- ``TEMPLATE`` indica el tipo de construcción. Puede ser una aplicación, una biblioteca, o simplemente subdirectorios.
- ``TARGET`` es el nombre de la aplicación o biblioteca.
- ``QT`` se usa para indicar qué bibliotecas (módulos Qt) están siendo usados en este proyecto. Dado que nuestra primera aplicación es una pequeña interfaz gráfica de usuario, necesitamos usar los módulos ``QtCore`` y ``QtGui``.

### Importando objetos de la biblioteca
Al crear una aplicación básica de Qt, usamos la clase ``QApplication``, de la cual [podemos consultar su referencia aquí](https://doc.qt.io/qt-5/qapplication.html). Si observas, indica la línea de ``qmake`` que debemos incluir si queremos usarla, en este caso importando el módulo ``widgets``.