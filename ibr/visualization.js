/**
 * @fileoverview This file takes data from sessionStorage from binToJs.js and visualize them using three.js
 * @author Shuang Li
 */

// Creating the scene
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 10000 );
var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

// Importing uploaded data
var material1 = new THREE.LineBasicMaterial( { color: 0x0000ff } );
var points = [];
layerCoordinates = JSON.parse(sessionStorage.getItem('layerCoordinates'));
for (x in layerCoordinates){
    points.push( new THREE.Vector3( layerCoordinates[x][0], layerCoordinates[x][1], 0 ) );
}

var geometry = new THREE.BufferGeometry().setFromPoints( points );
var line = new THREE.LineLoop( geometry, material1 );
scene.add( line );

camera.position.set( 0, 0, 7000 );
camera.lookAt( 0, 0, 0 );

// Rendering the scene
function animate() {
	requestAnimationFrame( animate );
	renderer.render( scene, camera );
}
animate();

function back() {
    window.location.href = "index.html";
}