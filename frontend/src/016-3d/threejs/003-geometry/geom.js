//           Geometrías a bajo nivel en ThreeJS

// Variables globales
var renderer;
var scene;
var camera;

function init() {
    scene = new THREE.Scene();

    camera = new THREE.PerspectiveCamera(
        95, window.innerWidth / window.innerHeight, 0.1, 1000
    );

    renderer = new THREE.WebGLRenderer();
    renderer.setClearColor(0x000000, 1);
    renderer.setSize(window.innerWidth, window.innerHeight);

    camera.position.x = 1;
    camera.position.y = 1;
    camera.position.z = 10;
    camera.lookAt(scene.position);

    // =================================================
    //                 THREE.Geometry()

    // Creamos una geometría base
    var geometry = new THREE.Geometry();
    // Añadimos tres vectores en la propiedad 'vertices'
    geometry.vertices.push(
        new THREE.Vector3(-10, 10, 0),
        new THREE.Vector3(-10, -10, 0),
        new THREE.Vector3(10, -10, 0)
    );
    // Añadimos una cara en la propiedad 'faces'
    // seleccionando el número de los vértices
    geometry.faces.push( new THREE.Face3(0, 1, 2));

    // ==================================================

    var material = new THREE.MeshBasicMaterial({color: 0x00ff00});
    var triangle = new THREE.Mesh( geometry, material );
    scene.add( triangle );


    // ==================================================
    //                 THREE.BufferGeometry()

    var geometry2 = new THREE.BufferGeometry();
    // Creamos la forma de un cuadrado simple. Se delimitan 6 puntos
    // debido a que construimos dos triángulos y cada vértice necesita
    // aparecer una vez por triángulo.
    var vertices2 = new Float32Array( [
        -1.0, -1.0,  1.0,
         1.0, -1.0,  1.0,
         1.0,  1.0,  1.0,

         1.0,  1.0,  1.0,
        -1.0,  1.0,  1.0,
        -1.0, -1.0,  1.0
    ] );

    // itemSize = 3 debido a que hay 3 valores (componentes) por vértice
    geometry2.addAttribute("position",
    	                   new THREE.BufferAttribute( vertices2, 3 )
    );

    // ==================================================


    material2 = new THREE.MeshBasicMaterial({color: 0xF3FFE2});
    var square = new THREE.Mesh( geometry2, material2 );
    scene.add( square );


    var spotLight = new THREE.SpotLight(0xffffff);
    spotLight.position.set(10, 20, 20);
    spotLight.castShadow = false;  // Activamos la emisión de sombras
    scene.add(spotLight);  // Añadimos la luz a la escena

    document.body.appendChild(renderer.domElement);
    render();
}

function render() {
    requestAnimationFrame(render);
    renderer.render(scene, camera);
}

function handleResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}


window.onload = init;

window.addEventListener('resize', handleResize, false);
