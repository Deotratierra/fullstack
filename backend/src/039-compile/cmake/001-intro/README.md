## Introducción a CMake

CMake es una herramienta multiplataforma para generar instrucciones de compilación de código. Para compilar código, en Linux es muy popular Make y en Windows los proyectos de Visual Studio. CMake ofrece una abstracción para generar los archivos de compilación dependiendo del sistema operativo:

Sin CMake, el proceso es el siguiente:
- Linux: escribimos un `Makefile` y compilamos con `make`
- Windows: creamos un proyecto de Visual Studio y compilamos con el mismo programa.

Con CMake, abstraemos el proceso:
- Escribimos CMake:
    - Linux: se genera el `Makefile` y compilamos con `make`.
    - VisualStudio: se genera el proyecto de Visual Studio y compilamos.

### `CMakeLists.txt`
En CMake las configuraciones estan centralizadas por defecto en un archivo llamado `CMakeLists.txt`. Este se encuentra en el directorio central del proyecto. Normalmente con CMake los proyectos se construyen en un directorio diferente al del código fuente. Es corriente crear una carpeta `build/` en la raíz del proyecto. De esta forma, si tenemos un proyecto con CMake ya descomprimido haríamos lo siguiente.

```bash
mkdir build
cd build
cmake ..
# Compilamos con make, ninja, nmake...
```

### `cmake-gui`
También es posible instalar una interfaz gráfica con la cual podemos configurar la construcción de nuestros proyectos.

> Para abrirla en sistemas Linux ejecutamos `cmake-gui`

### Instalación

> Podemos comprobar la versión, si ya está instalado, ejecutando `cmake -version`

#### Debian

```bash
sudo apt-get install cmake
```

- Interfaz: `sudo apt-get install cmake-gui`
