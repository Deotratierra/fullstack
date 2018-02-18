
//             Introducción a ThreeJS

// Creación de una escena:
var scene = new THREE.Scene();

// Creación de una cámara
var camera = new THREE.PerspectiveCamera(
    75, window.innerWidth / window.innerHeight, 0.1, 1000
);

// Renderizador
var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

// ================================================

// Añadimos geometría
var geometry = new THREE.BoxGeometry( 1, 1, 1 );
var material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
var cube = new THREE.Mesh( geometry, material );
scene.add( cube );

// Cambiamos la cámara de posición
camera.position.z = 5;
camera.position.x = 9;

function render() {
    renderer.render( scene, camera );
    requestAnimationFrame( animate );
}
render();