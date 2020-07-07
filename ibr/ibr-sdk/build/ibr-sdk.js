/**
 * @fileoverview This file contains functions that render given ibr binary
 data to (array of) THREE objects that can be used in browser.
 * @author shuanglihtk@google.com (Shuang Li)
 */

import {OrbitControls} from
  './../../../node_modules/three/examples/jsm/controls/OrbitControls.js';

// the length of one 3D coordinates (x, y, z) in the coordinate lookup float
// array
const ONE_POINT = 3;
// the length of two 3D coordinates (x, y, z) in the coordinate lookup float
// array
const TWO_POINTS = 6;

// separate floor's z-coordinate by 100 unit length
const FLOOR_HEIGHT = 300;

(function(global, factory) {
typeof exports === 'object' && typeof module !== 'undefined' ?
factory(exports) :
typeof define === 'function' && define.amd ? define(['exports'], factory) :
(global = global || self, factory(global.IBRSDK = {}));
}(window, (function(exports) {
  'use strict';

  let scene;

  /**
   * Create a side bar for layer and structure navigation.
   * @param {binary} IBRRawData Raw data from IBR binary data file.
   * @param {HTMLElement} parentElement Parent element to attach the sidebar to.
   */
  function createSidebar(IBRRawData, parentElement) {
    const ibrData = InternalBuildingRepresentation.read(
        new Pbf(IBRRawData));
    // for datafiles that have top level name is ""
    if (ibrData.name === '') {
      ibrData.name = 'ibrData.name';
    }
    const li = document.createElement('li'); // list element container
    parentElement.appendChild(li);
    const rootSpan = createLabel('span', ibrData.name, li);
    rootSpan.setAttribute('class', 'arrow');
    li.appendChild(rootSpan);
    const ul = document.createElement('ul');
    ul.setAttribute('class', 'nested');
    ul.setAttribute('id', ibrData.name);
    li.appendChild(ul);
    rootSpan.addEventListener('click', function() {
      rootSpan.parentElement.querySelector('.nested').classList
          .toggle('active');
      rootSpan.classList.toggle('expanded-arrow');
    });
    // root structure index 0
    const curStructure = renderSingleIBRStructure(ibrData, 0);
    drawSingleStructureSidebar(curStructure, ibrData.name);
  }

  /**
   * Generate Scene configured to display IBR data.
   * @param {HTMLElement} parentElement parent HTML element that the
   visualization will be append on.
   * @return {Object} scene Scene generated to
   */
  function generateScene(parentElement) {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(
        75, window.innerWidth / window.innerHeight, 0.1, 10000 );
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize( window.innerWidth, window.innerHeight );
    parentElement.appendChild( renderer.domElement );
    const controls = new OrbitControls( camera, renderer.domElement );
    controls.target.set( 0, 0.5, 0 );
    controls.update();
    controls.enablePan = false;
    controls.enableDamping = true;
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

    return scene;
  }

  /**
   * Create a new HTML Label Tag based on given name string and attach it to
   * given parent tag.
   * @param {string} tagName Type of tag to be created.
   * @param {string} name InnerHTML of the Label tag.
   * @param {tag} parentTag Tag to be attached to by the newly created label
    tag.
   * @param {string} [forId=undefined] ID to be set as the value of the newly
    created label tag's for attribute. Needed if Label tag is created for a
    checkbox.
   * @return {tag} Newly created Label tag.
   */
  function createLabel(tagName, name, parentTag, forId = undefined) {
    const label = document.createElement(tagName);
    if (forId) {
      label.setAttribute('for', forId);
    }
    label.innerHTML = name;
    parentTag.appendChild(label);
    return label;
  }

  //  function renderLayer

  /**
   * Create checkboxes for given structure's layers and child structures.
   * @param {Object} curStructure the structure generated from
   renderSingleIBRStructure() that will be added to sidebar.
   * @param {String} structureName the name of the structure being processed.
   */
  function drawSingleStructureSidebar(curStructure, structureName) {
    // Create checkbox for each layer
    if (curStructure['layers'].size !== 0) {
      for ( const [layerName, layer] of
        Object.entries(curStructure['layers']) ) {
        const checkBox = document.createElement('INPUT');
        const div = document.createElement('DIV');
        checkBox.setAttribute('type', 'checkbox');
        checkBox.setAttribute('id', structureName + '_' + layerName);
        div.appendChild(checkBox);
        createLabel('label', layerName, div, structureName + '_' +
        layerName);
        document.getElementById(structureName).appendChild(div);
        checkBox.addEventListener('change', function() {
          if (checkBox.checked) {
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
    for ( let structureIndex = 0; structureIndex <
    curStructure['structures'].length; structureIndex++ ) {
      const li = document.createElement('li');
      document.getElementById(structureName).appendChild(li);
      const label = createLabel('span',
          curStructure['structures'][structureIndex].name, li);
      label.setAttribute('class', 'arrow');
      li.appendChild(label);
      const ul = document.createElement('ul');
      ul.setAttribute('class', 'nested');
      ul.setAttribute('id', curStructure['structures'][structureIndex].name);
      li.appendChild(ul);
      label.addEventListener('click', function() {
        label.parentElement.querySelector('.nested').classList.toggle('active');
        label.classList.toggle('expanded-arrow');
        if (label.getAttribute('value') == null) {
          event.stopPropagation();
          const structure = renderSingleIBRStructure(
              curStructure['structures'][structureIndex],
              structureIndex, scene);
          drawSingleStructureSidebar(structure,
              curStructure['structures'][structureIndex].name);
          label.setAttribute('value', '0');
        }
      });
    }
  }

  /**
   * Parse top level of decoded IBR Object into structures.
   * @param {binary} IBRRawData Raw data from IBR binary data file.
   * @param {number} structureIndex Index of current structure(floor).
   * @param {HTMLElement} parentElement parent HTML element that the
    visualization will be append on.
   */
  function renderTopIBRStructure(IBRRawData, structureIndex, parentElement) {
    scene = generateScene(parentElement);
    const ibrData = InternalBuildingRepresentation.read(
        new Pbf(IBRRawData));
    const curStructure = {};
    // Visualization layers of current structure
    curStructure['layers'] = renderLayerAndSetToInvisible( ibrData,
        structureIndex, scene );
    // Sub-structures of the current structure
    curStructure['structures'] = [];
    for ( const struct of ibrData.structures ) {
      curStructure['structures'].push( struct );
    }
  }

  /**
   * Parse current IBR Object into structures.
   * @param {Object} ibrData decoded IBR object.
   * @param {number} structureIndex Index of current structure(floor).
   * @return {Map.<String, List.<Object>>} Map of list of layers and
   structures.
   */
  function renderSingleIBRStructure(ibrData, structureIndex) {
    const curStructure = {};
    // Visualization layers of current structure
    curStructure['layers'] = renderLayerAndSetToInvisible( ibrData,
        structureIndex);
    // Sub-structures of the current structure
    curStructure['structures'] = [];
    for ( const struct of ibrData.structures ) {
      curStructure['structures'].push( struct );
    }
    return curStructure;
  }

  /**
   * Swap endianness of 32bit numbers.
   * @param {number} val 32 bit number to be swapped.
   * @return {number} 32bit number in swapped endianness.
   */
  function swap32(val) {
    return ((val & 0xFF) << 24) |
               ((val & 0xFF00) << 8) |
               ((val >> 8) & 0xFF00) |
               ((val >> 24) & 0xFF);
  }

  // List of colors from jquery.color.js plugin
  const Colors = {};
  Colors.names = ['#00ffff',
    '#f0ffff',
    '#f5f5dc',
    '#000000',
    '#0000ff',
    '#a52a2a',
    '#00ffff',
    '#00008b',
    '#008b8b',
    '#a9a9a9',
    '#006400',
    '#bdb76b',
    '#8b008b',
    '#556b2f',
    '#ff8c00',
    '#9932cc',
    '#e9967a',
    '#9400d3',
    '#ff00ff',
    '#ffd700',
    '#008000',
    '#4b0082',
    '#f0e68c',
    '#add8e6',
    '#e0ffff',
    '#90ee90',
    '#d3d3d3',
    '#ffb6c1',
    '#ffffe0',
    '#00ff00',
    '#ff00ff',
    '#800000',
    '#000080',
    '#808000',
    '#ffa500',
    '#ffc0cb',
    '#800080',
    '#800080',
    '#ff0000',
    '#c0c0c0',
    '#ffffff',
    '#ffff00',
  ];

  Colors.random = function() {
    const result = this.names[Math.floor( Math.random() *
    (this.names.length - 1) )];
    return result;
  };

  /**
     * Converts decoded ibr structure data into three.js Line objects
     and add them to scene.
     * @param {Object} structure structures decoded from raw ibr data.
     * @param {number} structureIndex overall index of the structure.
     * @return {Map.<String, List.<Object>>} objects Layer name and
     corresponding list of three.js Line objects.
     */
  function renderLayerAndSetToInvisible(structure, structureIndex) {
    // Check if structure contains any visualization data
    if ( structure.visualization.length === 0 ||
    structure.coordinates_lookup == null) {
      return {};
    }

    // Decode Indices from data.visualization[].coordinate_indices
    let coordsIndexList; let coordsRangeBuffer; let coordsRange;
    const coordsRangeList = [];
    for (const visLayer of structure.visualization) {
      coordsIndexList = visLayer.coordinate_indices;
      coordsRangeBuffer = coordsIndexList.buffer.slice(
          coordsIndexList.byteOffset,
          coordsIndexList.byteOffset + coordsIndexList.length);
      coordsRange = new Uint32Array(coordsRangeBuffer);
      for (let i = 0; i < coordsRange.length; i++) {
        coordsRange[i] = swap32(coordsRange[i]);
      }
      coordsRangeList.push(coordsRange);
    }

    // Decode Coordinates from data.coordinates_lookup
    const coordsLookup = structure.coordinates_lookup;
    const coordsLookupBuffer = coordsLookup.buffer.slice(
        coordsLookup.byteOffset, coordsLookup.byteOffset +
        coordsLookup.length);
    const coordsLookupDV = new DataView(coordsLookupBuffer);
    const coordsLookupList = [];
    for (let i = 0; i < coordsLookup.length / 4; i += 4) {
      coordsLookupList.push(coordsLookupDV.getFloat32(i, false));
    }

    // Read multiple ranges from Visualization.coordinates array
    const layerCoordinates = [];
    for (const coordsRangeItem of coordsRangeList) {
      const layerPH = [];
      for (let i = 0; i < coordsRangeItem.length; i += 2) {
        const coordsLine = [];
        for (let j = coordsRangeItem[i]; j <= coordsRangeItem[i + 1];
          j += ONE_POINT) {
          coordsLine.push(coordsLookupList[j]);
          coordsLine.push(coordsLookupList[j + 1]);
          coordsLine.push(coordsLookupList[j + 2]);
        }
        layerPH.push(coordsLine);
      }
      layerCoordinates.push(layerPH);
    }

    // Render data into three.js objects
    const materials = [];
    for (let i = 0; i < structure.visualization.length - 1; i++) {
      materials.push(new THREE.LineBasicMaterial(
          {color: Colors.random()} ));
    }
    const objects = {};
    for (let i = 0; i < layerCoordinates.length; i++) {
      objects[structure.visualization[i].id] = [];
      const lineSegmentsGeometry = [];
      for (const line of layerCoordinates[i]) {
        const linePoints = [];
        for (let j = 0; j < line.length; j += ONE_POINT) {
          linePoints.push( new THREE.Vector3( line[j], line[j + 1],
              line[j + 2] + FLOOR_HEIGHT * structureIndex ) );
        }
        const geometry = new THREE.BufferGeometry().setFromPoints(
            linePoints );
        if (line.length === TWO_POINTS) {
          // group geometries for performance reason
          lineSegmentsGeometry.push( geometry );
        } else {
          const lineLoop = new THREE.LineLoop( geometry, materials[i] );
          lineLoop.visible = false;
          scene.add( lineLoop );
          objects[structure.visualization[i].id].push( lineLoop );
        }
      }
      if (lineSegmentsGeometry.length > 0) {
        const geometries = THREE.BufferGeometryUtils.mergeBufferGeometries(
            lineSegmentsGeometry );
        const lineSegments = new THREE.LineSegments( geometries, materials[i] );
        lineSegments.visible = false;
        scene.add( lineSegments );
        objects[structure.visualization[i].id].push( lineSegments );
      }
    }
    return objects;
  }

  exports.createSidebar = createSidebar;
  exports.generateScene = generateScene;
  exports.drawSingleStructureSidebar = drawSingleStructureSidebar;
  exports.renderTopIBRStructure = renderTopIBRStructure;
  exports.renderLayerAndSetToInvisible = renderLayerAndSetToInvisible;

  Object.defineProperty(exports, '__esModule', {value: true});
})));
