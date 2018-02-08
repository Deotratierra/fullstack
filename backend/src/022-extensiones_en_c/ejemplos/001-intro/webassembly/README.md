## Introducción a WebAssembly
Para trabajar con WebAssembly lo primero que tenemos que hacer es [instalar el compilador Emscripten](https://kripken.github.io/emscripten-site/docs/getting_started/downloads.html):

```
git clone https://github.com/juj/emsdk.git
cd emsdk
./emsdk install --build=Release sdk-incoming-64bit binaryen-master-64bit
./emsdk activate --build=Release sdk-incoming-64bit binaryen-master-64bit
source ./emsdk_env.sh
```

La última instrucción añadirá unas cuantas variables al `PATH`, para poder utilizar el compilador fácilmente.

### Hola mundo
```
mkdir hola_mundo
cd hola_mundo
echo '#include <stdio.h>' > hola.c
echo 'int main(int argc, char ** argv) {' >> hola.c
echo '    printf("Hello, world!\n");' >> hola.c
echo '}' >> hola.c

emcc hola.c -s WASM=1 -o hola.html
```

La última instrucción compila el código `.c` en `.wasm` y `.js`, además de proveer un archivo `.html` en el cual aparece una terminal donde se ejecuta el código. Si se abre de la forma usual no funcionará, para ello, tenemos que ejecutar un pequeño servidor. Aquí tienes dos opciones:
- `emrun --no_browser --port 8765 .`
- `python -m SimpleHTTPServer 8765`

Verás una terminal si accedes a http://localhost:8765/

El código WebAssembly sólo está soportado por las últimas versiones de Navegadores como Mozilla o Firefox. Si no ves nada en la terminal prueba a actualizar a la última versión.

> Fuentes:
> - https://hacks.mozilla.org/2017/02/a-cartoon-intro-to-webassembly/
> - https://labnotes.panderalabs.com/learning-how-to-learn-webassembly-7743663ed4d0
> - http://webassembly.org/getting-started/js-api/
> - https://github.com/mbasso/awesome-wasm/blob/master/README.md

