## Geometría en ThreeJS
La geometría en ThreeJS define la forma en la que los objetos son dibujados. Esta se compone de una colección de vértices y a veces caras las cuales combinan tres vértices en la cara de un triángulo.

Puedes crear tu propia geometría personalizada definiendo esos vértices y caras por ti mismo, pero ThreeJS tiene una variedad de formas comunes para acceder y establecer sus propiedades en su construcción.

### Geometría base
#### [`Geometry`](https://threejs.org/docs/index.html#api/core/Geometry)
Se encuentra en el núcleo de la biblioteca. Es la clase base para todas las geometrías simples, pero no para las geometrías de Buffer, que heredan de [`BufferGeometry`](https://threejs.org/docs/index.html#api/core/BufferGeometry).

Podemos añadir vértices añadiendo vectores al array de la propiedad `vertices` de una clase `Geometry`. Luego podemos seleccionar los vértices para construir una cara y ya tendremos una geometría personalizada lista para añadirle un material:

```javascript
var geometry = new THREE.Geometry();
geometry.vertices.push(
    new THREE.Vector3(-10, 10, 0),
    new THREE.Vector3(-10, -10, 0),
    new THREE.Vector3(10, -10, 0)
);
geometry.faces.push( new THREE.Face3(0, 1, 2));
var material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
var triangle = new THREE.Mesh( geometry, material );
scene.add( triangle );
```

#### [`BufferGeometry`](https://threejs.org/docs/#api/core/BufferGeometry)
La otra clase base de geometría. Esta optimizada para obtener un mayor rendimiento, pero los vértices no son directamente accesibles. La mejora de rendimiento se obtiene almacenando los valores de los vértices en memoria, por lo cual esta información no debe pasar a través de la GPU.

```javascript
var geometry = new THREE.BufferGeometry();
// Creamos la forma de un cuadrado simple. We duplicate the top left and bottom right
// vertices because each vertex needs to appear once per triangle.
var vertices = new Float32Array( [
    -1.0, -1.0,  1.0,
     1.0, -1.0,  1.0,
     1.0,  1.0,  1.0,

     1.0,  1.0,  1.0,
    -1.0,  1.0,  1.0,
    -1.0, -1.0,  1.0
] );

// itemSize = 3 because there are 3 values (components) per vertex
geometry.addAttribute( 'position', new THREE.BufferAttribute( vertices, 3 ) );
```


### Geometrías primitivas incorporadas
ThreeJS incorpora muchos tipos de geometrías primitivas. Aquí se encuentran algunos ejemplos:

#### [`PlaneGeometry`](https://threejs.org/docs/index.html#api/geometries/PlaneGeometry)
Geometría de un plano de forma cuadrada. Toma 4 argumentos: ancho, largo, número de segmentos del ancho y número de segmentos del largo.

> Los números de segmentos se refiere al número de divisiones que se realizan de una sóla línea. Por ejemplo, para un círculo, a mayor número de divisiones mayor precisión en la forma, pero más costoso es el renderizado.

#### [`BoxGeometry`](https://threejs.org/docs/index.html#api/geometries/BoxGeometry)
Geometría de un cubo. Toma 6 argumentos: ancho, alto, profundidad y el número de segmentos de cada uno de los 3 argumentos anteriores.

#### [`CircleGeometry`](https://threejs.org/docs/index.html#api/geometries/CircleGeometry)
Geometría de un círculo. Toma 4 argumentos:
- `radius`: Radio del círculo.
- `segments`: Número de segumentos triangulares que componen al círculo.
- `thetaStart`: El ángulo de comienzo para el primer segmento del círculo.
- `thetaLenght`: El ángulo central del círculo. Por defecto es `Math.PI*2`, el cual construye un círculo completo. Se puede decrecentar para formar menos de un círculo.

#### [`SphereGeometry`](https://threejs.org/docs/index.html#api/geometries/SphereGeometry)
La esfera funciona de la misma forma que el círculo añadiendo dos dimensiones para los segmentos además de la posibilidad de establecer el ángulo de comienzo y el ángulo de dibujo en ambas dimensiones:
- `radius`: Radio de la esfera. Por defecto 1.
- `widthSegments`: Número de segmentos horizontales. El valor mínimo es 3 y por defecto 8.
- `heightSegments`: Número de segmentos verticales. El valor mínimo es 2 y por defecto 6.
- `phiStart`: Especifica el ángulo horizontal de comienzo. Por defecto es 0.
- `phiLength`: Especifica el ángulo de barrido horizontal. Por defecto es `Math.PI * 2`.
- `thetaStart`: Especifica el ángulo vertical de comienzo. Por defecto es 0.
-  `thetaLength`: Especifica el ángulo vertical de barrido. Por defecto es `Math.PI`.

> Existen más geometrías pero toman los mismos tipos de valores que se han visto anteriormente.




> Fuentes:
> - http://blog.cjgammon.com/threejs-geometry