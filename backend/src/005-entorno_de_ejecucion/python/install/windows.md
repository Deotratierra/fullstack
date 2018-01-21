## Instalar Python en Windows
> NOTA: Las versiones superiores a Python3.4 no funcionan en WindowsXP.

### Instalador gráfico
La forma más fácil de instalar Python en Windows es ir a https://www.python.org/downloads/windows/, elegir la versión, descargarla y ejecutarla con el instalador por defecto.

### Instalar mediante línea de comandos
1. [Buscar aquí](https://www.python.org/ftp/python/) el número de versión (dentro de su carpeta) y el patch que queremos.
2. Descargamos `wget` para Windows: https://eternallybored.org/misc/wget/
3. Ejecutar los siguientes comandos, dependiendo del número de versión/patch que queremos:
```
wget https://www.python.org/ftp/python/<NUMERO.DE.VERSIÓN>/<nombre_del_archivo_comprimido_con_patch>.exe/msi
<nombre_del_archivo_comprimido_con_patch>.exe/msi
```

Tras estos comandos se lanzará el instalador gŕafico.

> Esta opción no es 100% línea de comandos pero permite mayor flexibilidad en cuanto a a versión que queremos descargar.

_______________________________________________

### Agregar Python al PATH
- Sólo en CMD actual: `set PATH=%PATH%;<ruta/al/ejecutable/python.exe>`
- Permanentemente:
    - WindowsXP: Mi PC -> Propiedades -> Avanzado -> Variables de entorno -> Path -> Editar. Agrega `;<ruta/al/ejecutable/python.exe>`.

