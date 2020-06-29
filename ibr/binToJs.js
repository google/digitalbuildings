/**
 * @fileoverview This file takes a binary wire format ibr file, decode the
 information and store data in sessionStorage for visualization use
 * @author shuanglihtk@google.com (Shuang Li)
 */

import {OrbitControls} from
  './node_modules/three/examples/jsm/controls/OrbitControls.js';

/**
 * Setup THREE.js environment and extract top level structure once an IBR
 file is given.
 */
function onChooseFile() {
  if (typeof window.FileReader !== 'function') {
    throw new Error('The file API isn\'t supported on this browser.');
  }
  const file = document.getElementById('fileForUpload').files[0];
  if (file) {
    const fr = new FileReader();
    fr.onload = function(evt) {
      const ibrData = evt.target.result;
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera( 75, window.innerWidth /
      window.innerHeight, 0.1, 10000 );
      const renderer = new THREE.WebGLRenderer();
      renderer.setSize( window.innerWidth, window.innerHeight );
      document.body.appendChild( renderer.domElement );
      const controls = new OrbitControls( camera, renderer.domElement );
      controls.target.set( 0, 0.5, 0 );
      controls.update();
      controls.enablePan = false;
      controls.enableDamping = true;
      const structures = IBRSDK.unpackStructure( ibrData );
      const layers = [];
      for ( const structure of structures ) {
        layers.push( IBRSDK.renderLayer(structure) );
      }
      for ( const layer of layers ) {
        for ( const line of layer ) {
          scene.add( line );
        }
      }
      camera.position.set( 0, 0, 7000 );
      camera.lookAt( 0, 0, 0 );
      animate();

      /**
        * Renders the scene.
        */
      function animate() {
        requestAnimationFrame( animate );
        controls.update();
        renderer.render( scene, camera );
      }
    };
    fr.readAsArrayBuffer(file);
  }
}
document.getElementById('fileForUpload')
    .addEventListener('change', onChooseFile);
