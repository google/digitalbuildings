/**
 * @fileoverview This file contains functions that render given ibr binary
 data to (array of) THREE objects that can be used in browser.
 * @author shuanglihtk@google.com (Shuang Li)
 */

// the length of one 3D coordinates (x, y, z) in the coordinate lookup float
// array
const ONE_POINT = 3;
// the length of two 3D coordinates (x, y, z) in the coordinate lookup float
// array
const TWO_POINTS = 6;

(function(global, factory) {
typeof exports === 'object' && typeof module !== 'undefined' ?
factory(exports) :
typeof define === 'function' && define.amd ? define(['exports'], factory) :
(global = global || self, factory(global.IBRSDK = {}));
}(window, (function(exports) {
  'use strict';

  /**
     * Decode raw ibr data into structures.
     * @param {Byte} data Binary data read directly from .ibr file
     * @return {Array.<Object>} structures List of structure objects
     generated from input ibr data
     */
  function unpackStructure(data) {
    const deserializedData = InternalBuildingRepresentation.read(
        new Pbf(data));
    let structures = [];
    structures.push( deserializedData );
    if ( deserializedData.structures.length > 0 ) {
      structures = deserializedData.structures;
    }
    return structures;
  }

  /**
   * Swap endianness of 32bit numbers.
   * @param {number} val Number to be converted endianness.
   * @return {number} 32 bit number with reverse engianness.
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
    '#8b0000',
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
     * Converts decoded ibr structure data into three.js Line objects.
     * @param {Object} structure structures decoded from raw ibr data
     * @return {Array.<Line>} lines List of three.js Line objects generated
     from input ibr data
     */
  function renderLayer(structure) {
    // Decode Indices from data.visualization[].coordinate_indices
    let coordsIndexList; let coordsRangeBuffer; let coordsRange;
    const coordsRangeList = [];
    for (const visLayer of structure.visualization) {
      coordsIndexList = visLayer.coordinate_indices;
      coordsRangeBuffer = coordsIndexList.buffer.slice(
          coordsIndexList.byteOffset,
          coordsIndexList.byteOffset+coordsIndexList.length);
      coordsRange = new Uint32Array(coordsRangeBuffer);
      for (let i = 0; i < coordsRange.length; i++) {
        coordsRange[i] = swap32(coordsRange[i]);
      }
      coordsRangeList.push(coordsRange);
    }

    // Decode Coordinates from data.coordinates_lookup
    const coordsLookup = structure.coordinates_lookup;
    const coordsLookupBuffer = coordsLookup.buffer.slice(
        coordsLookup.byteOffset, coordsLookup.byteOffset+coordsLookup.length);
    const coordsLookupDV = new DataView(coordsLookupBuffer);
    const coordsLookupList = [];
    for (let i = 0; i < coordsLookup.length/4; i+=4) {
      coordsLookupList.push(coordsLookupDV.getFloat32(i, false));
    }

    // Read multiple ranges from Visualization.coordinates array and store
    // them in sessionStorage for visualization later
    const layerCoordinates = [];
    for (const coordsRangeItem of coordsRangeList) {
      const layerPH = [];
      for (let i = 0; i < coordsRangeItem.length; i+=2) {
        const coordsLine = [];
        for (let j = coordsRangeItem[i]; j <= coordsRangeItem[i+1];
          j+=ONE_POINT) {
          coordsLine.push(coordsLookupList[j]);
          coordsLine.push(coordsLookupList[j+1]);
          coordsLine.push(coordsLookupList[j+2]);
        }
        layerPH.push(coordsLine);
      }
      layerCoordinates.push(layerPH);
    }

    // Render data into three.js objects
    const materials = [];
    for (let i = 0; i < structure.visualization.length-1; i++) {
      materials.push(new THREE.LineBasicMaterial( {color: Colors.random()} ));
    }
    const objects = [];
    for (let i = 0; i < layerCoordinates.length; i++) {
      const lineSegments = [];
      for (const line of layerCoordinates[i]) {
        const linePoints = [];
        for (let j = 0; j < line.length; j+=ONE_POINT) {
          linePoints.push( new THREE.Vector3( line[j], line[j+1],
              line[j+2] ) );
        }
        const geometry = new THREE.BufferGeometry().setFromPoints(
            linePoints );
        if (line.length === TWO_POINTS) {
          // group geometries for performance reason
          lineSegments.push( geometry );
        } else {
          objects.push( new THREE.LineLoop( geometry, materials[i] ) );
        }
      }
      if (lineSegments.length > 0) {
        const geometries = THREE.BufferGeometryUtils.mergeBufferGeometries(
            lineSegments );
        objects.push( new THREE.LineSegments( geometries, materials[i] ) );
      }
    }
    return objects;
  }

  exports.renderLayer = renderLayer;
  exports.unpackStructure = unpackStructure;

  Object.defineProperty(exports, '__esModule', {value: true});
})));
