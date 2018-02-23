## Figuras geométricas en ThreeJS

Para crear figuras, lo primero que necesitamos es un material del cual estará hecho la figura. Si venimos de entornos de trabajo 3D como Blender, ya estaremos acostumbrados a trabajar con materiales, pero es algo que desde el campo de la programación no resulta tan intuitivo al principio.

>El término **textura** hace referencia a la apariencia general de un objeto tridimensional. En definitiva, aquello quehace que algo que debe ser de cuero parezca de cuero o algo que debe simular piedra se vea como piedra. Pero no solo el color es lo que hace que un objeto parezca del material del que debe ser. También es importante elacabado y la luz. Algunos objetos rebotan la luz, como los espejos. Algunos refractan la luz, como el cristal. Y algunos absorben más la luz, como los objetos opacos. Debemos tener en cuenta que, si solo contásemos como condicionante con el color de un objeto ¿cómo diferenciaríamos, por ejemplo, un objeto de piedra de un objeto de aluminio si los dosson de color gris? Precisamente porque la piedra no refleja la luz y el aluminio sí. Por lo tanto, a la hora de hacer tantopiedra como aluminio en 3D tendremos que tener en cuenta como interacciona cada uno de los materiales con la luz. De esta manera se planteas dos términos bien diferenciados en el mundo de la infografía 3D: material y textura.

Dicho esto, empecemos desde el principio para familiarizarnos con ThreeJS. Vamos a crear un cubo y le vamos a colocar un suelo debajo.

### [`PlaneGeometry`](https://threejs.org/docs/index.html#api/geometries/PlaneGeometry)
Clase para generar geometrías planas. Toma 4 argumentos:
- `width`: Ancho en X del plano.
- `height`: Alto en Y del plano.
- `widthSegments`
- `heightSegments`

Observar en el ejemplo ubicado en este directorio como seguimos el patrón de crear una geometría (`planeGeometry`, `cubeGeometry`), añadirle un material ([`MeshLambertMaterial`](https://threejs.org/docs/index.html#api/materials/MeshLambertMaterial) en ambos casos) y llamar al objeto [`Mesh`](https://threejs.org/docs/index.html#api/objects/Mesh) para unir material y geometría en un objeto.

También es interesante notar como se usan las propiedades `rotation` y `position` para controlar la posición y la rotación de los objetos, así como las propiedades `castShadow` (determina si un objeto puede emitir sombra) y `receiveShadow` (determina si un objeto puede recibir sombra).

Por último observar que la función `handleResize()` es muy útil y reutilizable, ya que permite mantener las proporciones de los elementos desplegados cuando se redimensiona la ventana del navegador.

> Fuentes:
> - https://www.scribd.com/document/364954706/Trucos-Para-Materiales-y-Texturas-de-Diseno-3D-de-Arquitectura
> - Essential ThreeJS - [Jos Dirksen](https://github.com/josdirksen)
> - https://github.com/josdirksen/essential-threejs/blob/master/chapter-01/01.02-simple-mesh.html