// the length of one 3D coordinates (x, y, z) in the coordinate lookup float
// array
const ONE_POINT = 3;

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

/**
 * Constructor of Visualization Class.
 * @param {Object} visualizationData single visualization data from JSON
 Object decoded using Pbf library from raw ibr binary data.
 */
function Visualization( visualizationData, coordsLookup ) {
  this.id = visualizationData.id;
  this.data = visualizationData.data;

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

  this.encodingType = visualizationData.encoding_type;
  this.imageData = visualizationData.image_data;

  // Set Line Coordinates for Visualization
  const coordsRangeItem = this.coordinateIndices;
  const coordsLine = [];
  for (let i = 0; i < coordsRangeItem.length; i += 2) {
    for (let j = coordsRangeItem[i]; j <= coordsRangeItem[i + 1];
      j += ONE_POINT) {
      coordsLine.push(coordsLookup[j]);
      coordsLine.push(coordsLookup[j + 1]);
      coordsLine.push(coordsLookup[j + 2]);
    }
  }
  this.setLineCoordinates(coordsLine);
}

Object.assign( Visualization.prototype, {

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
  setLineCoordinates: function( lineCoordinates ) {
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
    json.coordinate_indices = new Uint8Array( tempCoordinateIndices.buffer );
    return json;
  },

} );

export {Visualization, swap32, ONE_POINT};
