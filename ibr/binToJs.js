/**
 * @fileoverview This file takes a binary wire format ibr file, decode the information and store data in sessionStorage for visualization use
 * @author shuanglihtk@google.com (Shuang Li)
 */

import { OrbitControls } from './node_modules/three/examples/jsm/controls/OrbitControls.js';

/**
 * Create a new HTML Label Tag based on given name string and attach it to given parent tag.
 * @param {String} name InnerHTML of the Label tag.
 * @param {Tag} parentTag Tag to be attached to by the newly created label tag.
 * @param {String} forId ID to be set as the value of the newly created label tag's for attribute. Needed if Label tag is created for a checkbox.
 * @return {Tag} label Newly created Label tag.
 */
function createLabel(name, parentTag, forId=undefined) {
    var label = document.createElement('LABEL');
    if (forId) {
        label.setAttribute('for', forId);
    }
    label.innerHTML = name;
    parentTag.appendChild(label);
    return label;
}

/**
 * Create checkboxes for given structure's layers and child structures.
 * @param {Object} structureData Structure to be extracted and visualized.
 * @param {String} curStructureId ID of the HTML div element to attach the new structure's data.
 * @param {THREE.Scene Object} scene object to attach the THREE.js objects generated from structure layer data
 */
function extractSingleStructureData(structureData, curStructureId, scene) {

    var curStructure = IBRSDK.unpackStructure( structureData );
    // Create checkbox for each layer
    if (curStructure['layers'].length !== 0) {
        for ( const [layerName, layer] of Object.entries(curStructure['layers']) ) {
            for ( const line of layer ) {
                line.visible = false;
                scene.add( line );
            }
            var checkBox = document.createElement('INPUT');
            var div = document.createElement('DIV');
            checkBox.setAttribute('type', 'checkbox');
            checkBox.setAttribute('id', layerName);
            div.appendChild(checkBox);
            //debug
            div.style.padding = "0px 0px 0px 10px";
            createLabel(layerName, div, layerName);
            document.getElementById(curStructureId).appendChild(div);
            checkBox.addEventListener('change', function() {
                if (this.checked) {
                    for ( const line of layer ) {
                        line.visible = true;
                    }
                } else {
                    for ( const line of layer ) {
                        line.visible = false;
                    }
                }
            });
        }
    }

    // Create label for each child structure
    for ( const structure of curStructure['structures'] ) {
        var div = document.createElement('DIV');
        div.setAttribute('id', structure.name);
        var label = createLabel(structure.name, document.getElementById(curStructureId));
        div.style.padding = "0px 0px 0px 10px";
        label.style.padding = "0px 0px 0px 10px";
        document.getElementById(curStructureId).appendChild(div);
        label.addEventListener('click', function(event) {
            event.stopPropagation();
            extractSingleStructureData(structure, structure.name, scene);
        });
    }
}

/**
 * Setup THREE.js environment and extract top level structure once an IBR file is given.
 */
function onChooseFile() {
    if (typeof window.FileReader !== 'function')
        throw ("The file API isn't supported on this browser.");
    let file = document.getElementById("fileForUpload").files[0];
    if (file) {
        let fr = new FileReader();
        fr.onload = function (evt) {
            var ibrData = InternalBuildingRepresentation.read(new Pbf( evt.target.result ));
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

            if (ibrData.name === "") {
                ibrData.name = "ibrData.name"; // for datafiles that have top level name is ""
            }
            createLabel(ibrData.name, document.getElementById('layerList'));
            var div = document.createElement('DIV');
            div.setAttribute('id', ibrData.name);
            document.getElementById('layerList').appendChild(div);
            extractSingleStructureData(ibrData, ibrData.name, scene, 1);

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
