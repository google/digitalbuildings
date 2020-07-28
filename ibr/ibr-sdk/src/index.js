/**
 * @fileoverview This file contains functions that render given IBR buffer
  to THREE objects that can be displayed in the UI.
 * @author shuanglihtk@google.com (Shuang Li)
 */

'use strict';

import {OrbitControls} from
  './../node_modules/three/examples/jsm/controls/OrbitControls.js';
import {BufferGeometryUtils} from
  './../node_modules/three/examples/jsm/utils/BufferGeometryUtils.js';
import {IBRObject} from './IBRObject.js';
import {Colors} from './colors.js';
import {ONE_POINT, TWO_POINTS, FLOOR_HEIGHT} from './constants.js';

/**
 * Create a side bar for visualization and structure navigation.
 * @param {IBRObject} ibrObject IBRObject created from IBR binary data file.
 * @param {HTMLElement} parentElement Parent element to attach the sidebar to.
 * @param {Object} scene The Scene Object that all THREE objects are
  rendered on.
 */
function createSidebar(ibrObject, parentElement, scene) {
  const li = document.createElement('li'); // list element container
  parentElement.appendChild(li);
  const rootSpan = createLabel('span', ibrObject.getName(), li);
  rootSpan.setAttribute('class', 'arrow');
  li.appendChild(rootSpan);
  const ul = document.createElement('ul');
  ul.setAttribute('class', 'nested');
  ul.setAttribute('id', ibrObject.getName());
  li.appendChild(ul);
  rootSpan.addEventListener('click', function() {
    rootSpan.parentElement.querySelector('.nested').classList
        .toggle('active');
    rootSpan.classList.toggle('expanded-arrow');
  });
  // root structure index 0
  const structure = renderSingleIBRStructure(ibrObject, 0, scene);
  drawSingleStructureSidebar(structure, ibrObject.getName(), scene);
}

/**
 * Generate Scene configured to display IBR data.
 * @param {HTMLElement} parentElement parent HTML element that the
 visualization will be append on.
 * @return {Object} scene The scene that has all THREE objects rendered on.
 */
function generateScene(parentElement) {
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(
      75, window.innerWidth / window.innerHeight, 0.1, 10000);
  const renderer = new THREE.WebGLRenderer();
  renderer.setSize(window.innerWidth, window.innerHeight);
  parentElement.appendChild(renderer.domElement);
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.target.set(0, 0.5, 0);
  controls.update();
  controls.enablePan = true;
  controls.enableDamping = true;
  camera.position.set(0, 7000, 0);
  camera.lookAt(0, 0, 0);
  animate();
  window.addEventListener('resize', onWindowResize, false);

  /**
  * Renders the scene.
  */
  function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
  }

  /**
  * Resize the scene.
  */
  function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
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

/**
 * Create checkboxes for given structure's visualizations and child structures.
 * @param {Object} structure the structure generated from
 renderSingleIBRStructure() that will be added to sidebar.
 * @param {String} structureName the name of the structure being processed.
 * @param {Object} scene The Scene Object that all THREE objects are
  rendered on.
 */
function drawSingleStructureSidebar(structure, structureName, scene) {
  // Create checkbox for Blocking Grid
  if (structure['blockingGrid']) {
    createCheckboxForVisualization(
        structure['visualizations'][structure['blockingGrid']],
        structure['blockingGrid'], structureName);
  }
  // Create checkbox for each visualization
  if (structure['visualizations'].size !== 0) {
    for (const [visualizationName, visualization] of
      Object.entries(structure['visualizations'])) {
      createCheckboxForVisualization(visualization, visualizationName,
          structureName);
    }
  }

  // Create label for each child structure
  for (let structureIndex = 0; structureIndex <
  structure['structures'].length; structureIndex++) {
    const li = document.createElement('li');
    document.getElementById(structureName).appendChild(li);
    const label = createLabel('span',
        structure['structures'][structureIndex].name, li);
    label.setAttribute('class', 'arrow');
    li.appendChild(label);
    const ul = document.createElement('ul');
    ul.setAttribute('class', 'nested');
    ul.setAttribute('id', structure['structures'][structureIndex].name);
    li.appendChild(ul);
    label.addEventListener('click', function() {
      label.parentElement.querySelector('.nested').classList.toggle('active');
      label.classList.toggle('expanded-arrow');
      if (label.getAttribute('value') == null) {
        event.stopPropagation();
        const curStructure = renderSingleIBRStructure(
            new IBRObject(structure['structures'][structureIndex]),
            structureIndex, scene);
        drawSingleStructureSidebar(curStructure,
            structure['structures'][structureIndex].name, scene);
        label.setAttribute('value', '0');
      }
    });
  }
}

/**
 * Initialize IBRObject from input IBR raw data in binary format.
 * @param {Buffer} ibrRawData binary IBR data from uploaded IBR file.
 * @return {IBRObject} ibrObject IBRObject generated from input binary.
 */
function init(ibrRawData) {
  const ibrData = InternalBuildingRepresentation.read(
      new Pbf(ibrRawData));
  const ibrObject = new IBRObject(ibrData);
  return ibrObject;
}

/**
 * Enable Export and parse top level of decoded IBR Object into structures.
 * @param {IBRObject} ibrObject IBRObject created from input IBR binary data
 file.
 * @param {number} structureIndex Index of current structure(floor).
 * @param {HTMLElement} parentElement parent HTML element that the
  visualization will be append on.
 * @return {Object} scene The Scene Object that all THREE objects are
 rendered on.
 */
function render(ibrObject, structureIndex, parentElement) {
  const scene = generateScene(parentElement);
  document.getElementById('dwn-btn').style.display = 'block';
  document.getElementById('filename').style.display = 'block';
  // Visualization visualizations of current structure
  renderVisualizations(ibrObject, structureIndex, scene);
  // scene for createSidebar use, both functions need to use the
  // same scene object to associate checkboxes with visualizations.
  return scene;
}

/**
 * Parse current IBR Object into structures.
 * @param {IBRObject} ibrObject IBRObject created from current structure data.
 * @param {number} structureIndex Index of current structure(floor).
 * @param {Object} scene The Scene Object that all THREE objects are
  rendered on.
 * @return {Map.<String, List.<Object>>} Map of list of visualizations and
 structures.
 */
function renderSingleIBRStructure(ibrObject, structureIndex, scene) {
  const structure = {};
  if (ibrObject.hasBlockingGrid) {
    structure['blockingGridID'] = ibrObject.getBlockingGrid().getID();
  }
  // Visualizations of current structure
  structure['visualizations'] = renderVisualizations(ibrObject,
      structureIndex, scene);
  // Sub-structures of the current structure
  structure['structures'] = ibrObject.getSubStructures();
  return structure;
}

/**
 * Render all visualization layers (including blocking grid if applicable)
 in the given IBRObject.
 * @param {IBRObject} structure IBRObject generated from current
 structure data.
 * @param {number} structureIndex overall index of the structure.
 * @param {Object} scene The Scene Object that all THREE objects are
  rendered on.
 * @return {Map.<String, List.<Object>>} objects Visualization name and
 corresponding list of three.js Line objects.
 */
function renderVisualizations(structure, structureIndex, scene) {
  const objects = {};

  // Check if structure contains any visualization data
  if (!structure.hasVisualizations ||
  !structure.hasCoordinatesLookup) {
    return objects;
  }

  // Render blocking grid in the structure
  if (structure.hasBlockingGrid) {
    const visualizationPH = structure.getBlockingGrid().getVisualization().
        getLineCoordinates();
    const visualizationObjects = renderVisualization(visualizationPH,
        structureIndex, scene);
    objects[structure.getBlockingGrid().getVisualization().getID()] =
    visualizationObjects;
  }

  // Render visualizations in the structure
  for (const visualization of structure.getVisualizations().values()) {
    const visualizationPH = visualization.getLineCoordinates();
    const visualizationObjects = renderVisualization(visualizationPH,
        structureIndex, scene);
    objects[visualization.getID()] = visualizationObjects;
  }

  return objects;
}

/**
 * Converts the visualization data into three.js Line objects
 and add them to scene with visibility set to false.
 * @param {List.<List.<Number>>} visualizationCoordinates List of line
 coordinates of the visualization to be rendered.
 * @param {number} structureIndex overall index of the structure.
 * @param {Object} scene The Scene Object that all THREE objects are
  rendered on.
 * @return {List.<Object>} objects List of three.js Line objects.
 */
function renderVisualization(visualizationCoordinates, structureIndex, scene) {
  // Render data into three.js objects
  const material = new THREE.LineBasicMaterial({color: Colors.random()});
  const objects = [];
  const lineSegmentsGeometry = [];
  for (const line of visualizationCoordinates) {
    const linePoints = [];
    for (let j = 0; j < line.length; j += ONE_POINT) {
      // Swapped y, z coordinates of all points to allow x-y plane rotation
      // changed sign of z coordinates to improve y-z plane rotation
      linePoints.push(new THREE.Vector3(line[j],
          line[j + 2] + FLOOR_HEIGHT * structureIndex, -line[j + 1]));
    }
    const geometry = new THREE.BufferGeometry().setFromPoints(
        linePoints);
    if (line.length === TWO_POINTS) {
      // group geometries for performance improvement
      lineSegmentsGeometry.push(geometry);
    } else {
      const lineLoop = new THREE.LineLoop(geometry, material);
      lineLoop.visible = false;
      scene.add(lineLoop);
      objects.push(lineLoop);
    }
  }
  if (lineSegmentsGeometry.length > 0) {
    const geometries = BufferGeometryUtils.mergeBufferGeometries(
        lineSegmentsGeometry);
    const lineSegments = new THREE.LineSegments(geometries, material);
    lineSegments.visible = false;
    scene.add(lineSegments);
    objects.push(lineSegments);
  }
  return objects;
}

/**
 * Serialize IBRObject object to binary format.
 * @param {IBRObject} ibrObject The IBRObject to be saved back to binary
 format.
 * @return {Buffer} buffer binary representation of IBRObject object.
 */
function saveToBuffer(ibrObject) {
  const json = ibrObject.toJson();
  const pbf = new Pbf();
  InternalBuildingRepresentation.write(json, pbf);
  const buffer = pbf.finish();
  return buffer;
}


/**
 * Create checkboxes for given visualization.
 * @param {Object} visualization the visualization object to be
 added to the sidebar.
 * @param {String} visualizationName the name of the visualization being
 processed.
 * @param {String} structureName the name of parent structure of the
 visualization.
 */
function createCheckboxForVisualization(visualization, visualizationName,
    structureName) {
  const checkBox = document.createElement('INPUT');
  const div = document.createElement('DIV');
  checkBox.setAttribute('type', 'checkbox');
  checkBox.setAttribute('id', structureName + '_' + visualizationName);
  div.appendChild(checkBox);
  createLabel('label', visualizationName, div, structureName + '_' +
  visualizationName);
  document.getElementById(structureName).appendChild(div);
  checkBox.addEventListener('change', function() {
    if (checkBox.checked) {
      for (const line of visualization) {
        line.visible = true;
      }
    } else {
      for (const line of visualization) {
        line.visible = false;
      }
    }
  });
}

/**
 * Render top level structure in IBRObject and create a side bar for
 visualization and structure navigation.
 * @param {IBRObject} ibrObject IBRObject created from IBR binary data file.
 * @param {number} structureIndex Index of current structure(floor).
 * @param {HTMLElement} renderParentElement Parent element to attach the
 rendering to.
 * @param {HTMLElement} sidebarParentElement Parent element to attach the
 sidebar to.
 */
function renderAndCreateSidebar(ibrObject, structureIndex,
    renderParentElement, sidebarParentElement) {
  const scene = render(ibrObject, structureIndex, renderParentElement);
  createSidebar(ibrObject, sidebarParentElement, scene);
}

export {createSidebar, renderAndCreateSidebar, init, render, saveToBuffer,
renderSingleIBRStructure};
