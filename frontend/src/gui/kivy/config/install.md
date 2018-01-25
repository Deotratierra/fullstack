## Instalación de Kivy
Aquí se proporcionan guías para configurar un entorno de desarrollo completo de Kivy.

### Linux
> [Referencia oficial](https://kivy.org/docs/installation/installation-linux.html)

#### Debian
> ¡Sólo disponible a partir de Jessie!

1. Instalamos Kivy junto al directorio de ejemplos:
```
sudo echo "deb http://ppa.launchpad.net/kivy-team/kivy/ubuntu xenial main" > /etc/apt/sources.list.d/kivy-team-ubuntu-kivy-bionic.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A863D2D6
sudo apt-get update
sudo apt-get install python3-kivy
```

2. Lo siguiente es probar la instalación. Para ello:
```
git clone https://github.com/kivy/kivy.git
cd kivy/examples/demo/kivycatalog
python3 main.py
```

Aparecerá un catálogo con muchos ejemplos de Kivy que pueden ser editados. En el subdirectorio `examples` puedes comprobarlos uno a uno.

> Si te ocurre cualquier fallo en la renderización chequea la referencia oficial o busca en internet.

___________________________________

### Widgets de ampliación
La biblioteca [kivymd](https://gitlab.com/kivymd/KivyMD) cual proporciona widgets siguiendo los patrones de la guía de estilo de diseño de aplicaciones de Google [Material Design](https://material.io/guidelines/):
```
git clone https://gitlab.com/kivymd/KivyMD
cd KivyMD && sudo python3 setup.py install
cd demos/kitchen_sink
python3 main.py
```

___________________________________

