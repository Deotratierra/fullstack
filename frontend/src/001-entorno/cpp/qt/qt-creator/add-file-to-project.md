## Añadir archivos a proyectos en Qt Creator

- Con el proyecto abierto, vamos a ``File`` -> ``New File or Project`` -> ``C++`` -> ``C++ Source File``.

Si observamos ahora el archivo con extensión ``.pro`` del proyecto, se habrá añadido el archivo al array de archivos fuente (variable ``SOURCES``). Podemos añadir archivos manualmente con:

```
HEADERS += first_file.h second_file.h
SOURCES += first_file.cpp second_file.cpp
```