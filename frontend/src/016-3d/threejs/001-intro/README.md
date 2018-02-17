## Introducción a [ThreeJS](https://threejs.org/)

Para ser capaces de renderizar cualquier cosa con ThreeJS, necesitamos 3 cosas: una escena, una cámara y un renderizador. En este pequeño tutorial cubriremos cada elemento de una forma general.

### Escena
##### [Referencia](https://threejs.org/docs/index.html#api/scenes/Scene)
- Creación de una escena:
```javascript
var scene = new THREE.Scene();
```

- Cambiar el color de fondo: `scene.background = new THREE.Color( 0x333333 );` 

### Cámara
Existen varios tipos de cámaras en ThreeJS.

#### [`PerspectiveCamera`](https://threejs.org/docs/index.html#api/cameras/PerspectiveCamera)
Esta cámara está diseñada para simular la visión de los seres humanos, es la proyección más común para renderizar en 3D.

- Inicializar:
```javascript
var camera = new THREE.PerspectiveCamera(
    75, window.innerWidth / window.innerHeight, 0.1, 1000
);
```

Esta toma 4 argumentos:
- `fov`: Campo de visión (**F**ield **o**f **v**iew) vertical de la cámara. Es la extensión de la escena que se verá en la demostración en cualquier momento de la escena. El valor viene dado en grados.
- `aspect`: Ratio de visión. Casi siempre se coloca el ancho entre el alto de la pantalla completa para no deformar la imagen.
- `near`: Señala lo más cerca que puede estar un elemento de la cámara para ser renderizado. Por defecto es `0.1`.
- `far`: Señala lo más lejos que puede estar un elemento de la cámara para ser renderizado. Por defecto es `2000`.

### Renderizador
Este nos permite desplegar la imagen en la pantalla.

#### [`WebGLRenderer`](https://threejs.org/docs/#api/renderers/WebGLRenderer)
Es el más utilizado, aunque existen otros pero se usan más que nada para usuarios que no tienen soporte de [WebGL](https://es.wikipedia.org/wiki/WebGL) en su navegador.

- Inicializar:
```javascript
var renderer = new THREE.WebGLRenderer();
```

Podemos establecer el tamaño de la pantalla desplegada usando:
```javascript
renderer.setSize(window.innerWidth, window.innerHeight)
```

Luego debemos insertar el objeto `canvas` creado por el renderizador al momento de instanciarse así:
```javascript
document.body.appendChild(renderer.domElement);
```

_______________________________

Con los elementos anteriores tendremos una pantalla negra desplegada el navegador, pero no mostrará nada más. Para ello habría que añadir algunos objetos a la escena. Puedes ver el ejemplo de este directorio con un cubo verde añadido, pero no entraremos en detalles.

