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
 * Initialize IBRObject from input IBR raw data in binary format.
 * @param {Buffer} ibrRawData binary IBR data from uploaded IBR file.
 * @return {IBRObject} ibrObject IBRObject generated from input binary.
 */
function init(ibrRawData) {
  const ibrData = InternalBuildingRepresentation.read(
      new Pbf(ibrRawData));
  console.log(ibrData);
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
  structure['blockingGrid'] = renderBlockingGrid(ibrObject,
      structureIndex, scene);
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
  const objects = new Map();

  // Check if structure contains any visualization data
  if (!structure.hasVisualizations ||
  !structure.hasCoordinatesLookup) {
    return objects;
  }

  // Render visualizations in the structure
  for (const visualization of structure.getVisualizations().values()) {
    const visualizationPH = visualization.getLineCoordinates();
    const visualizationObjects = renderVisualization(visualizationPH,
        structureIndex, scene);
    objects.set(visualization.getID(), visualizationObjects);
  }

  return objects;
}

/**
 * Render blocking grid in the given IBRObject.
 * @param {IBRObject} structure IBRObject generated from current
 structure data.
 * @param {number} structureIndex overall index of the structure.
 * @param {Object} scene The Scene Object that all THREE objects are
  rendered on.
 * @return {Map.<String, List.<Object>>} objects Blocking grid name and
 corresponding list of three.js Line objects.
 */
function renderBlockingGrid(structure, structureIndex, scene) {
  let objects = null;

  // Render blocking grid in the structure
  if (structure.hasBlockingGrid) {
    objects = {};
    const visualizationPH = structure.getBlockingGrid().getVisualization().
        getLineCoordinates();
    const visualizationObjects = renderVisualization(visualizationPH,
        structureIndex, scene);
    objects['Blocking Grid'] = visualizationObjects;
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

export {init, render, saveToBuffer, renderSingleIBRStructure};

