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
import {ONE_POINT, TWO_POINTS, FLOOR_HEIGHT, BLOCKING_GRID_NAME, BOUNDARY_NAME,
  ONE_TRIANGLE, IMAGE_PADDING} from './constants.js';

/**
 * Generate Scene configured to display IBR data.
 * @param {HTMLElement} parentElement parent HTML element that the
 visualization will be append on.
 * @return {Object} scene The scene that has all THREE objects rendered on.
 */
function generateScene(parentElement) {
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0xffffff);
  const light = new THREE.DirectionalLight(0xffffff, 1);
  light.position.setScalar(10);
  scene.add(light);
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
  camera.position.set(0, 5000, 0);
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
 * @param {String} filename Name of the input IBR file.
 * @return {IBRObject} ibrObject IBRObject generated from input binary.
 */
function init(ibrRawData, filename) {
  const ibrData = InternalBuildingRepresentation.read(
      new Pbf(ibrRawData));
  const ibrObject = new IBRObject(ibrData, filename);
  return ibrObject;
}

/**
 * Enable Export and parse top level of decoded IBR Object into structures.
 * @param {IBRObject} ibrObject IBRObject created from input IBR binary data
 file.
 * @param {HTMLElement} parentElement parent HTML element that the
  visualization will be append on.
 * @param {Map.<String, List<Mesh>>} spaceLib Space library stores space
 name and mesh object(s).
 * @param {Map.<String, List.<String, Line>>} connectionLib Boundary name and
 corresponding list of neighbor names and three.js Line object.
 * @return {Object} scene The Scene Object that all THREE objects are
 rendered on.
 */
function render(ibrObject, parentElement, spaceLib, connectionLib) {
  const scene = generateScene(parentElement);
  document.getElementById('sidebar-title').innerHTML = ibrObject.getName();
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
 * @param {Map.<String, List<Mesh>>} spaceLib Space library stores space
 name and mesh object(s).
 * @param {Map.<String, List.<String, Line>>} connectionLib Boundary name and
 corresponding list of neighbor names and three.js Line object.
 * @return {Map.<String, List.<Object>>} Map of list of visualizations and
 structures.
 */
function renderSingleIBRStructure(ibrObject, structureIndex, scene, spaceLib,
    connectionLib) {
  const structure = {};
  structure['blockingGrid'] = renderBlockingGrid(ibrObject,
      structureIndex, scene);
  structure['boundary'] = renderBoundary(ibrObject,
      structureIndex, scene, spaceLib, connectionLib);
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
    let visualizationObjects;
    if (visualization.getEncodingType() !==
        InternalBuildingRepresentation.Visualization.EncodingType[
            'BITMAP_IMAGE'].value) {
      const visualizationPH = visualization.getLineCoordinates();
      visualizationObjects = renderLines(visualizationPH,
          structureIndex, scene);
    } else {
      visualizationObjects = renderImages(visualization, scene);
    }
    objects.set(visualization.getID(), visualizationObjects);
  }

  return objects;
}

/**
 * Converts visualization image data into three.js Plane objects
 and add them to scene with visibility set to false.
 * @param {Object} visualization The visualization object from IBR structure.
 * @param {Object} scene The Scene Object that all THREE objects are
  rendered on.
 * @return {List.<Object>} objects List of three.js Plane objects.
 */
function renderImages(visualization, scene) {
  const objects = [];
  const imageBytes = visualization.getImageData().image;
  let binary = '';
  const len = imageBytes.byteLength;
  for (let i = 0; i < len; i++) {
    binary += String.fromCharCode(imageBytes[i]);
  }
  const imageBase64Encoded = btoa(binary);
  const planeGeometry = new THREE.PlaneGeometry(visualization.
      getImageData().length, visualization.getImageData().width);
  const texture = new THREE.TextureLoader().load(
      'data:image/jpeg;base64,' + imageBase64Encoded);
  const planeMaterial = new THREE.MeshLambertMaterial({map: texture});
  const plane = new THREE.Mesh(planeGeometry, planeMaterial);
  plane.receiveShadow = true;
  plane.position.set((visualization.getImageData().length)/2, IMAGE_PADDING,
      -(visualization.getImageData().width)/2);
  plane.rotation.x = -0.5 * Math.PI;
  plane.rotation.z = -1 * Math.PI;
  plane.visible = false;
  scene.add(plane);
  objects.push(plane);
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
    const visualizationObjects = renderLines(visualizationPH,
        structureIndex, scene);
    objects[BLOCKING_GRID_NAME] = visualizationObjects;
  }

  return objects;
}

/**
 * Render boundary in the given IBRObject.
 * 1. find neighbors
 * 2. check if any neighbors are rendered, if yes, take its color from spaceLib
 * 3. render this space with the color
 * 4. render connection with the color
 * @param {IBRObject} ibrObject IBRObject generated from current
 structure data.
 * @param {number} structureIndex overall index of the structure.
 * @param {Object} scene The Scene Object that all THREE objects are
  rendered on.
 * @param {Map.<String, List<Mesh>>} spaceLib Space library stores space
 name and mesh object(s).
 * @param {Map.<String, List.<String, Line>>} connectionLib Boundary name and
 corresponding list of neighbor names and three.js Line object.
 * @return {Map.<String, List.<Object>>} objects Boundary name and
 corresponding list of three.js Line objects.
 */
function renderBoundary(ibrObject, structureIndex, scene, spaceLib,
    connectionLib) {
  let objects = null;
  if (ibrObject.hasBoundary) {
    const curName = ibrObject.getName();
    connectionLib.set(curName, []);
    objects = {};
    const coordsRangeItem = ibrObject.getBoundary();
    const visualizationPH = [];
    for (let i = 0; i < coordsRangeItem.length; i += 2) {
      const coordsLine = [];
      for (let j = coordsRangeItem[i]; j <= coordsRangeItem[i + 1];
        j += ONE_POINT) {
        coordsLine.push(ibrObject.getCoordinates()[j]);
        coordsLine.push(ibrObject.getCoordinates()[j + 1]);
        coordsLine.push(ibrObject.getCoordinates()[j + 2]);
      }
      visualizationPH.push(coordsLine);
    }
    // Find neighbors
    const connections = ibrObject.getConnections();
    // Temporary way to retrieve floor number
    const floorNumber = Number(curName.split('-')[3]);
    const leftNeighborName = findLeftNeighbor(floorNumber, connections);
    const rightNeighborName = findRightNeighbor(floorNumber, connections);
    // check if any neighbors are rendered, if yes, take its color from spaceLib
    let color;
    for (const connection of connections) {
      const connectionName = connection.external_structure_id;
      if (connectionName && spaceLib.has(connectionName)) {
        color = spaceLib.get(connectionName)[0].material.color;
        break;
      }
    }
    // Render this space with the color
    const renderAsPolygon = ibrObject.structuralType ===
      InternalBuildingRepresentation.StructuralType['SPACE'].value;
    objects[BOUNDARY_NAME] = renderLines(
        visualizationPH,
        structureIndex,
        scene,
        renderAsPolygon,
        color);
    objects[BOUNDARY_NAME][0].name = curName;
    // Calculate current space center
    objects[BOUNDARY_NAME][0].geometry.computeBoundingBox();
    const thisCenter =
    objects[BOUNDARY_NAME][0].geometry.boundingBox.getCenter();
    // Calculate neighbor space center and create connectors
    if (leftNeighborName && spaceLib.has(leftNeighborName)) {
      if (!spaceLib.get(leftNeighborName)[0].geometry.boundingBox) {
        spaceLib.get(leftNeighborName)[0].geometry.computeBoundingBox();
      }
      const leftNeighborCenter =
      spaceLib.get(leftNeighborName)[0].geometry.boundingBox.getCenter();
      renderConnections(thisCenter, leftNeighborCenter, curName,
          leftNeighborName, connectionLib, color, scene);
    }
    if (rightNeighborName && spaceLib.has(rightNeighborName)) {
      if (!spaceLib.get(rightNeighborName)[0].geometry.boundingBox) {
        spaceLib.get(rightNeighborName)[0].geometry.computeBoundingBox();
      }
      const rightNeighborCenter =
      spaceLib.get(rightNeighborName)[0].geometry.boundingBox.getCenter();
      renderConnections(thisCenter, rightNeighborCenter, curName,
          rightNeighborName, connectionLib, color, scene);
    }
    spaceLib.set(curName, objects[BOUNDARY_NAME]);
  }
  return objects;
}

/**
 * Find the left neighbor of the structure in it's connections.
 * @param {Number} floorNumber Current structure's floor number.
 * @param {List<Object>} connections List of connections of the structure.
 * @return {String} Name of the left neighbor structure.
 */
function findLeftNeighbor(floorNumber, connections) {
  let left = -1;
  let leftNeighborName = null;
  for (const connection of connections) {
    const num = Number(connection.external_structure_id.split('-')[3]);
    if (num < floorNumber && num > left) {
      left = num;
      leftNeighborName = connection.external_structure_id;
    }
  }
  return leftNeighborName;
}

/**
 * Find the right neighbor of the structure in it's connections.
 * @param {Number} floorNumber Current structure's floor number.
 * @param {List<Object>} connections List of connections of the structure.
 * @return {String} Name of the right neighbor structure.
 */
function findRightNeighbor(floorNumber, connections) {
  let right = Number.MAX_SAFE_INTEGER;
  let rightNeighborName = null;
  for (const connection of connections) {
    const num = Number(connection.external_structure_id.split('-')[3]);
    if (num > floorNumber && num < right) {
      right = num;
      rightNeighborName = connection.external_structure_id;
    }
  }
  return rightNeighborName;
}

/**
 * Render a vertical connector with two end points.
 * @param {Vector3} thisCenter The center of the current structure.
 * @param {Vector3} neighborCenter The center of its neighbor structure.
 * @param {String} curName The name of the current structure.
 * @param {String} neighborName The name of its neighbor structure.
 * @param {Map.<String, List.<String, Line>>} connectionLib Boundary name and
 corresponding list of neighbor names and three.js Line object.
 * @param {Color} color Color of the vertical connector.
 * @param {Object} scene The Scene Object that all THREE objects are
  rendered on.
 */
function renderConnections(thisCenter, neighborCenter, curName, neighborName,
    connectionLib, color, scene) {
  const endPoints = [];
  endPoints.push(thisCenter);
  endPoints.push(neighborCenter);
  const geometry = new THREE.BufferGeometry().setFromPoints(endPoints);
  const material = new THREE.LineBasicMaterial({
    color: color,
  });
  const connector = new THREE.Line(geometry, material);
  connector.visible = false;
  scene.add(connector);
  connectionLib.get(curName).push([neighborName, connector]);
  connectionLib.get(neighborName).push([curName, connector]);
}

/**
 * Converts the visualization data into three.js Line objects
 and add them to scene with visibility set to false.
 * @param {List.<List.<Number>>} visualizationCoordinates List of line
 coordinates of the visualization to be rendered.
 * @param {number} structureIndex overall index of the structure.
 * @param {Object} scene The Scene Object that all THREE objects are
  rendered on.
 * @param {Boolean} renderAsPolygon If the lines currently being rendered are
 from the boundary field of the ibrObject.
 * @param {Color} color The color of the lines being rendered.
 * @return {List.<Object>} objects List of three.js Line objects.
 */
function renderLines(visualizationCoordinates, structureIndex, scene,
    renderAsPolygon=false, color=null) {
  // Render data into three.js objects
  if (!color) {
    color = Colors.random();
  }
  const lineMaterial = new THREE.LineBasicMaterial({color: color});
  const meshMaterial = new THREE.MeshBasicMaterial({color: color});
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
      let lineLoop = null;
      if (renderAsPolygon) {
        lineLoop = createPolygon(linePoints, meshMaterial);
      } else {
        lineLoop = new THREE.LineLoop(geometry, lineMaterial);
      }
      lineLoop.visible = false;
      scene.add(lineLoop);
      objects.push(lineLoop);
    }
  }
  if (lineSegmentsGeometry.length > 0) {
    const geometries = BufferGeometryUtils.mergeBufferGeometries(
        lineSegmentsGeometry);
    const lineSegments = new THREE.LineSegments(geometries, lineMaterial);
    lineSegments.visible = false;
    scene.add(lineSegments);
    objects.push(lineSegments);
  }
  return objects;
}

/**
 * Create Polygon Mesh Object from list of vertices.
 * @param {List.<Vector3>} poly List of vertices of the polygon.
 * @param {Object} material The material Mesh is going to be rendered in.
 * @return {Object} Polygon Mesh Object generated from vertices.
 */
function createPolygon(poly, material) {
  const shape = new THREE.Geometry();
  shape.vertices = poly;
  shape.faces = triangulatePoints(poly);
  return new THREE.Mesh(shape, material);
}

/**
 * Triangulate given vertices.
 * @param {List.<Vector3>} poly List of vertices of the polygon.
 * @return {List.<Face3>} faces List of triangles of the triangulation
 of the given vertices.
 */
function triangulatePoints(poly) {
  const pointsXZ = [];
  for (const point of poly) {
    pointsXZ.push(point.x, point.z * -1);
  }
  const triangles = earcut(pointsXZ);
  const faces = [];
  for (let i = 0; i < triangles.length; i+=ONE_TRIANGLE) {
    faces.push(new THREE.Face3(triangles[i], triangles[i+1],
        triangles[i+2]));
    faces.push(new THREE.Face3(triangles[i+2], triangles[i+1],
        triangles[i]));
  }
  return faces;
}

/**
 * Serialize IBRObject object to binary format.
 * @param {IBRObject} ibrObject The IBRObject to be saved back to binary
 format.
 * @param {List.<Boolean>} floorsToSave Boolean array representing the floors
 to be exported. If element at index i is true, the i-th floor will be
 exported.
 * @return {Buffer} buffer binary representation of IBRObject object.
 */
function saveToBuffer(ibrObject, floorsToSave) {
  console.log('saving to buffer');
  console.log(floorsToSave);
  let json = ibrObject.toJson();
  const structuresToSave = [];
  for (const i in floorsToSave) {
    if (floorsToSave[i]) {
      structuresToSave.push(json.structures[i]);
    }
  }

  if (structuresToSave.length === 1) {
    json = structuresToSave[0];
  } else {
    json.structures = structuresToSave;
  }

  const pbf = new Pbf();
  InternalBuildingRepresentation.write(json, pbf);
  const buffer = pbf.finish();

  return buffer;
}

export {init, render, saveToBuffer, renderSingleIBRStructure};

