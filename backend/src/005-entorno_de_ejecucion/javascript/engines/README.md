## Intérpretes Javascript

También conocidos como motores Javascript, interpretan el código Javascript, lo compilan a bytecode y ejecutan las instrucciones. El primer intérprete fue el [SpiderMonkey](https://en.wikipedia.org/wiki/SpiderMonkey), el cual implementaba Firefox hasta la versión 25. Tras esta, fue mejorado a TraceMonkey, provocando una optimización de entre 20 y 40 veces.

### Chrome V8
Es el intérprete más utilizado actualmente. Es el encargado de ejecutar NodeJS, navegadores como Chrome y Opera, además como aplicaciones como Electron, entre sus implementaciones más conocidas. Gracias al desarrollo de Google, se ha convertido en el intérprete de referencia. Está escrito en C++, implementa [ECMAScript](https://tc39.es/ecma262/) y [WebAssembly](https://webassembly.github.io/spec/core/) y puede correr de forma autónoma o incluido en cualquier aplicación C++.

Este intérprete posibilitó la creación de NodeJS (Javascript de lado del servidor), lo cual revolucionó el entorno Javascript, proveyéndole características para el lenguaje imposibles hasta entonces.

#### [Cómo funciona V8](https://github.com/mondeja/fullstack/blob/master/backend/src/005-entorno_de_ejecucion/javascript/engines/v8/how-works.md)

> Fuentes:
- [Intérprete Javascript](https://en.wikipedia.org/wiki/JavaScript_engine)
- [SpiderMonkey](https://en.wikipedia.org/wiki/SpiderMonkey)
- [Chrome V8](https://en.wikipedia.org/wiki/Chrome_V8)
- [V8](https://v8.dev/)
