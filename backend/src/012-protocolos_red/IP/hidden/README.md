## Ocultación de IP

Es posible ocultar nuestra IP al navegar usando diferentes técnicas.

__________________________

### Tor como proxy Socks5
Podemos usar el servicio de Tor para usar el cifrado en capas de cebolla que este programa ofrece, ya sea desde nuestro navegador preferido, usando peticiones en crudo, con Selenium... etc. 

Lo único que debemos hacer es redirigir todo el tráfico que deseamos ofuscar a través del socket `socks5://127.0.0.1:9050`, esto es, un socket con el protocolo [Socks5](https://es.wikipedia.org/wiki/SOCKS) en local a través del puerto `9050`.

#### Instalación
Para usar esta ténica es necesario instalar el servicio de Tor que correrá como un demonio en segundo plano (no confundir con el navegador, este no hace falta instalarlo).

##### Linux
1. Instalar: `sudo apt-get install tor`
2. Comprobar si Tor está corriendo como servicio: `sudo service tor status`

##### Windows
1. Descargar el navegador Tor desde [aquí](https://www.torproject.org/download/download.html.en) e instalar.
2. Abrimos la terminal como superusuarios: `Inicio` -> `Buscar` -> `cmd` -> <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + Click
3. La instalación habrá generado una carpeta llamada `Tor Browser`. Vamos a la carpeta que se encuentra dentro de `Tor Browser\Browser\TorBrowser\Tor` y ejecutamos `tor.exe -service install`.
4. Comprobar que funciona: `Inicio` -> `Buscar` -> `services.msc` -> <kbd>ENTER</kbd> -> Buscamos el servicio de nombre `Tor Win32 Service` y lo iniciamos si no está corriendo.

_________________

#### Usar con Firefox
`Menú` -> `Preferencias` -> `Avanzado` -> `Red` -> `Conexión` -> `Configuración` -> `Configuración manual del proxy`

- Servidor SOCKS: `127.0.0.1`
- Puerto: `9050`
- No usar proxy para: `localhost, 127.0.0.1`

__________________

#### Usar con Selenium y Firefox
```python
from selenium.webdriver import (
    Firefox,
    FirefoxProfile
)

profile = FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks_version", 5)
profile.set_preference("network.proxy.socks", '127.0.0.1')
profile.set_preference("network.proxy.socks_port", 9050)
profile.set_preference("network.proxy.socks_remote_dns", True)

driver = Firefox(profile)
```

__________________________

#### [Usar con libcurl](https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html)
```c
curl_easy_setopt(curl, CURLOPT_PROXY, "socks5://127.0.0.1:9050");
```

__________________________

### Comprobación de funcionamiento
Para comprobar que funciona simplemente hemos de consultar nuestra IP sin usar el proxy, lo cual nos mostrará la IP real, y usándolo para asegurarnos de que la IP cambia.

- Para ello podemos hacer peticiones a: `http://httpbin.org/ip`

___________________________

