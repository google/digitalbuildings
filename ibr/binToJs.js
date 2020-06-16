/**
 * @fileoverview This file takes a binary wire format ibr file, decode the information and store data in sessionStorage for visualization use
 * @author shuanglihtk@google.com (Shuang Li)
 */

function swap32(val) {
    return ((val & 0xFF) << 24)
           | ((val & 0xFF00) << 8)
           | ((val >> 8) & 0xFF00)
           | ((val >> 24) & 0xFF);
}

function onFileLoad(event) {
    var ibrData = event.target.result;
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 10000 );
    var renderer = new THREE.WebGLRenderer();
    renderer.setSize( window.innerWidth, window.innerHeight );
    document.body.appendChild( renderer.domElement );
    var lines = IBRSDK.renderLayer( ibrData );
    for (const line of lines) {
        scene.add(line);
    }
    camera.position.set( 0, 0, 7000 );
    camera.lookAt( 0, 0, 0 );
    animate();

    // Rendering the scene
    function animate() {
        requestAnimationFrame( animate );
        renderer.render( scene, camera );
    }
}

function onChooseFile(event, onLoadFileHandler) {
    if (typeof window.FileReader !== 'function')
        throw ("The file API isn't supported on this browser.");
    let input = event.target;
    if (!input)
        throw ("The browser does not properly implement the event object");
    if (!input.files)
        throw ("This browser does not support the `files` property of the file input.");
    if (!input.files[0])
        return undefined;
    let file = input.files[0];
    let fr = new FileReader();
    fr.onload = onLoadFileHandler;
    fr.readAsArrayBuffer(file);
}

