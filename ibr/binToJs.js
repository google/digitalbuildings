/**
 * @fileoverview This file takes a binary wire format ibr file, decode the information and store data in sessionStorage for visualization use
 * @author shuanglihtk@google.com (Shuang Li)
 */

import { OrbitControls } from './node_modules/three/examples/jsm/controls/OrbitControls.js';

function onChooseFile() {
    if (typeof window.FileReader !== 'function')
        throw ("The file API isn't supported on this browser.");
    let file = document.getElementById("fileForUpload").files[0];
    if (file) {
        let fr = new FileReader();
        fr.onload = function (evt) {
            var ibrData = evt.target.result;
            var scene = new THREE.Scene();
            var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 10000 );
            var renderer = new THREE.WebGLRenderer();
            renderer.setSize( window.innerWidth, window.innerHeight );
            document.body.appendChild( renderer.domElement );
            var controls = new OrbitControls( camera, renderer.domElement );
            controls.target.set( 0, 0.5, 0 );
            controls.update();
            controls.enablePan = false;
            controls.enableDamping = true;
            var structures = IBRSDK.unpackStructure( ibrData );
            var layers = [];
            for ( const structure of structures ) {
                layers.push( IBRSDK.renderLayer (structure) );
            }
            for ( const layer of layers ) {
                for ( const line of layer ) {
                    scene.add( line );
                }
            }
            camera.position.set( 0, 0, 7000 );
            camera.lookAt( 0, 0, 0 );
            animate();

            // Rendering the scene
            function animate() {
                requestAnimationFrame( animate );
                controls.update();
                renderer.render( scene, camera );
            }
        }
        fr.readAsArrayBuffer(file);
    }
}
document.getElementById('fileForUpload').addEventListener('change', onChooseFile);
