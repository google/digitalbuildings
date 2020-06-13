/**
 * @fileoverview This file takes data from sessionStorage from binToJs.js and visualize them using three.js
 * @author shuanglihtk@google.com (Shuang Li)
 */

// Creating the scene
(function () {
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 10000 );
    var renderer = new THREE.WebGLRenderer();
    renderer.setSize( window.innerWidth, window.innerHeight );
    document.body.appendChild( renderer.domElement );

    // Importing uploaded data
    var material1 = new THREE.LineBasicMaterial( { color: 0x0000ff } );
    var points = [];
    var numOfLines = JSON.parse(sessionStorage.getItem('numOfLines'));
    var geometry, line;
    for (var i = 0; i < numOfLines; i++) {
        layerCoordinates = JSON.parse(sessionStorage.getItem('layerCoordinates' + i));
        for (var x in layerCoordinates) {
            points.push( new THREE.Vector3( layerCoordinates[x][0], layerCoordinates[x][1], 0 ) );
        }
        geometry = new THREE.BufferGeometry().setFromPoints( points );
        line = new THREE.LineLoop( geometry, material1 );
        scene.add( line );
    }

    camera.position.set( 0, 0, 7000 );
    camera.lookAt( 0, 0, 0 );
    animate();

    // Rendering the scene
    function animate() {
        requestAnimationFrame( animate );
        renderer.render( scene, camera );
    }
})();

function back() {
    window.location.href = "index.html";
}