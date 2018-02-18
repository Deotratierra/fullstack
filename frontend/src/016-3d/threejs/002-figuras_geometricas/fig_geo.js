//             Figuras geométricas en ThreeJS

// Variables globales
    var renderer;
    var scene;
    var camera;

/**
 * Inicializa la escena, la cámara y los objetos. Se llama cuando
 * se carga la venta del navegador (ver abajo)
 */
function init() {
    // Creamos la escena
    scene = new THREE.Scene();

    // Creamos una cámara
    camera = new THREE.PerspectiveCamera(
    	45, window.innerWidth / window.innerHeight, 0.1, 1000
    );

    // Creamos el renderizador
    renderer = new THREE.WebGLRenderer();
    renderer.setClearColor(0x003800, 1.0); // Color de fondo del renderizado
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.shadowMapEnabled = true;  // Activación de mapas de sombras

    // Creamos el plano del suelo
    var planeGeometry = new THREE.PlaneGeometry(20, 20);
    // Le añadimos un material
    var planeMaterial = new THREE.MeshLambertMaterial({color: 0xcccccc});
    var plane = new THREE.Mesh(planeGeometry, planeMaterial);
    plane.receiveShadow = true; // Activamos la recepción de sombra en el plano
    // Rotamos y posicionamos el plano
    plane.rotation.x = -0.5 * Math.PI;
    plane.position.x = 0;
    plane.position.y = -2;
    plane.position.z = 0;
    // Añadimso el plano a la escena
    scene.add(plane);

    // Creamos un cubo
    var cubeGeometry = new THREE.BoxGeometry(6, 4, 6);
    var cubeMaterial = new THREE.MeshLambertMaterial({color: 'red'});
    var cube = new THREE.Mesh(cubeGeometry, cubeMaterial);
    cube.castShadow = true; // Activamos la emisión de sombras del cubo
    // Añadimos el cubo a la escena
    scene.add(cube);

    // Posicionamos y apuntamos la cámara hacia el centro de la escena
    camera.position.x = 15;
    camera.position.y = 16;
    camera.position.z = 13;
    camera.lookAt(scene.position);

    // Añadimos una luz concentrada
    var spotLight = new THREE.SpotLight(0xffffff);
    spotLight.position.set(10, 20, 20);
    spotLight.shadowCameraNear = 20;
    spotLight.shadowCameraFar = 50;
    spotLight.castShadow = true;  // Activamos la emisión de sombras
    scene.add(spotLight);  // Añadimos la luz a la escena

    // Añadimos el canvas renderizado al cuerpo del HTML
    document.body.appendChild(renderer.domElement);
    // Llamamos a la función de renderización.
    // Después del primer renderizado, el intervalo lo determina
    // la función requestAnimationFrame.
    render();
}
/**
 * Se llama cuando la escena necesita ser renderizada. Delega
 * en la función requestAnimationFrame para futuras renderizaciones.
 */
function render() {
    // render using requestAnimationFrame
    requestAnimationFrame(render);
    renderer.render(scene, camera);
}

/**
 * Manejador para redmensionar tanto la cámara como la matriz
 * de proyección cuando se redimensiona la ventana
 */
function handleResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

// Llama a la función init cuando la ventana se carga
window.onload = init;

// Llama a la función handleResize() cuando la ventana se redimensiona
window.addEventListener('resize', handleResize, false);


