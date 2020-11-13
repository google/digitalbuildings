import {ONE_POINT} from './constants.js';
import {swap32} from './util.js';

/**
 * Constructor of Visualization Class.
 * @param {Object} visualizationData single visualization data from JSON
 Object decoded using Pbf library from raw ibr binary data.
 * @param {List.<Number>} coordsLookup Coords Lookup from the parent structure.
 */
function Visualization(visualizationData, coordsLookup) {
  this.id = visualizationData.id;
  this.data = visualizationData.data;
  this.encodingType = visualizationData.encoding_type;

  if (visualizationData.image_data) {
    this.imageData = visualizationData.image_data;
  } else {
    // Decode Indices from data.visualization[].coordinate_indices
    const coordsIndexList = visualizationData.coordinate_indices;
    const coordsRangeBuffer = coordsIndexList.buffer.slice(
        coordsIndexList.byteOffset,
        coordsIndexList.byteOffset + coordsIndexList.length);
    const coordsRange = new Uint32Array(coordsRangeBuffer);
    for (let i = 0; i < coordsRange.length; i++) {
      coordsRange[i] = swap32(coordsRange[i]);
    }
    this.coordinateIndices = coordsRange;

    // Set Line Coordinates for Visualization
    const coordsRangeItem = this.coordinateIndices;
    const visualizationPH = [];
    for (let i = 0; i < coordsRangeItem.length; i += 2) {
      const coordsLine = [];
      for (let j = coordsRangeItem[i]; j <= coordsRangeItem[i + 1];
        j += ONE_POINT) {
        coordsLine.push(coordsLookup[j]);
        coordsLine.push(coordsLookup[j + 1]);
        coordsLine.push(coordsLookup[j + 2]);
      }
      visualizationPH.push(coordsLine);
    }
    this.setLineCoordinates(visualizationPH);
  }
}

Object.assign(Visualization.prototype, {

  constructor: Visualization,

  /**
   * Get the ID of the visualization.
   * @return {String} ID of the visualization.
   */
  getID: function() {
    return this.id;
  },

  /**
   * Get the data of the visualization.
   * @return {String} data of the visualization.
   */
  getData: function() {
    return this.data;
  },

  /**
   * Get the coordinates indices of the visualization.
   * @return {List.<number>} coordinates indices of the visualization.
   */
  getCoordinatesIndices: function() {
    return this.coordinateIndices;
  },

  /**
   * Get the encoding type of the visualization.
   * @return {number} encoding type of the visualization.
   */
  getEncodingType: function() {
    return this.encodingType;
  },

  /**
   * Get the image data of the visualization.
   * @return {Object} image data of the visualization.
   */
  getImageData: function() {
    return this.imageData;
  },

  /**
   * Set the line coordinates of the visualization during IBRObject
   construction.
   * @param {List.<List.<number>>} lineCoordinates list of list of end point
    coordinates that each represent a line during rendering.
   */
  setLineCoordinates: function(lineCoordinates) {
    this.lineCoordinates = lineCoordinates;
  },

  /**
   * Get the line coordinates of the visualization.
   * @return {List.<List.<number>>} list of list of end point coordinates that
    each represent a line during rendering.
   */
  getLineCoordinates: function() {
    return this.lineCoordinates;
  },

  /**
   * Convert Visualization data object to JSON format.
   * @return {JSONObject} JSON format of Visualization data object.
   */
  toJson: function() {
    const json = {};
    json.id = this.id;
    json.encoding_type = this.encodingType;
    json.image_data = this.imageData;
    json.data = this.data;
    const tempCoordinateIndices = this.coordinateIndices;
    for (let i = 0; i < tempCoordinateIndices.length; i++) {
      tempCoordinateIndices[i] = swap32(tempCoordinateIndices[i]);
    }
    json.coordinate_indices = new Uint8Array(tempCoordinateIndices.buffer);
    return json;
  },

});

export {Visualization};
