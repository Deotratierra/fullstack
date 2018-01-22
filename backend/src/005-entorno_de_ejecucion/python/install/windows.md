## Instalar Python en Windows
> NOTA: Las versiones superiores a Python3.4 no funcionan en WindowsXP.

### Instalador gráfico
La forma más fácil de instalar Python en Windows es ir a https://www.python.org/downloads/windows/, elegir la versión, descargarla y ejecutarla con el instalador por defecto.

### Instalar mediante línea de comandos
1. [Buscar aquí](https://www.python.org/ftp/python/) el número de versión (dentro de su carpeta) y el patch que queremos.
2. [Descargamos `wget` para Windows](https://eternallybored.org/misc/wget/)y lo colocamos en el directorio actual.
3. Ejecutar los siguientes comandos, dependiendo del número de versión/patch que queremos:
```
wget https://www.python.org/ftp/python/<NUMERO.DE.VERSIÓN>/<nombre_del_archivo_comprimido_con_patch>.exe/msi
<nombre_del_archivo_comprimido_con_patch>.exe/msi /passive PrependPath=1
```

> Todas las opciones del instalador [se encuentran aquí](https://docs.python.org/3/using/windows.html).

_______________________________________________

### Agregar Python al PATH
- Sólo en CMD actual: `set PATH=%PATH%;<ruta\al\directorio\del\ejecutable\>`
- Permanentemente:
    - WindowsXP: Mi PC -> Propiedades -> Avanzado -> Variables de entorno -> Path -> Editar. Agrega `;<ruta\al\directorio\del\ejecutable\>`.
    - Windows10: Buscar -> Agrega `Path` + <kbd>ENTER</kbd> -> Path -> Editar -> Nuevo. Agrega `<ruta\al\directorio\del\ejecutable\>`.

> Al instalar Python en Windows se crea un ejecutable `python.exe` en la carpeta de instalación (su ubicación depende de tu versión). Lo más recomendable es cambiar el nombre del ejecutable por el de tu versión (por ejemplo `python3.7.exe`, así podrás tener varias versiones de Python instaladas y llamarlas desde línea de comandos por su versión).

_______________________________________________