## Crear un demonio Unix en Python
La implementación más interesante de un demonio Unix en Python que he encontrado hasta la fecha se encuentra en [este repositorio](https://pagure.io/python-daemon/tree/master). Hay una copia del mismo de la versión `2.1.2` en este mismo directorio.

Para usarlo simplemente extraemos la biblioteca, copiamos el archivo `daemon/daemon.py` a nuestro proyecto y lo importamos: `from daemon import DaemonContext`.

### Configuración
Entre los parámetros que permite `DaemonContext`, los siguientes son los más relevantes:
- `stdin` / `stdout` / `stderr`: Son parámetros diferentes. Archivos por los cuales redirigir las salidas del demonio. Lo normal es redirigirlos a un log en `/var/log`. Los archivos deben ser abiertos con un modo mínimo de lectura (`"r"`) en el caso de `stdin` y un modo mínimo de escritura (`"w+"`) en los casos de `stdout` y `stderr`.
- `files_preserve`: Lista de archivos que no deben ser cerrados al arrancar el demonio. `None` por defecto.
- `chroot_directory`: Ruta completa a un directorio a establecer como directorio raíz del proceso. `None` por defecto.
- `working_directory`: Ruta completa al directorio de trabajo al cual el demonio debe cambiar al arrancar. `/` por defecto.


### Inicialización
Hay varias formas de inicializar el demonio, las siguientes son equivalentes entre sí:
```python
with DaemonContext(**kwargs):
    inicia_tu_programa()
```

```python
d = DaemonContext(**kwargs):
d.open()
inicia_tu_programa()
d.close()
```

```python
d = DaemonContext():
[d.key = value for key, value in kwargs.items()]
d.open()
inicia_tu_programa()
d.close()
```