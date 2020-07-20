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
 * Constructor of Layer Class.
 * @param {Objecy} layerData single layer data from JSON Object decoded using
 Pbf library from raw ibr binary data.
 */
function Layer( layerData ) {
  this.id = layerData.id;
  this.data = layerData.data;

  // Decode Indices from data.visualization[].coordinate_indices
  const coordsIndexList = layerData.coordinate_indices;
  const coordsRangeBuffer = coordsIndexList.buffer.slice(
      coordsIndexList.byteOffset,
      coordsIndexList.byteOffset + coordsIndexList.length);
  const coordsRange = new Uint32Array(coordsRangeBuffer);
  for (let i = 0; i < coordsRange.length; i++) {
    coordsRange[i] = swap32(coordsRange[i]);
  }
  this.coordinateIndices = coordsRange;

  this.encodingType = layerData.encoding_type;
  this.imageData = layerData.image_data;
  this.lineCoordinates = null;
}

Object.assign( Layer.prototype, {

  constructor: Layer,

  /**
   * Get the ID of the layer.
   * @return {String} ID of the layer.
   */
  getID: function() {
    return this.id;
  },

  /**
   * Get the data of the layer.
   * @return {String} data of the layer.
   */
  getData: function() {
    return this.data;
  },

  /**
   * Get the coordinates indices of the layer.
   * @return {List.<number>} coordinates indices of the layer.
   */
  getCoordinatesIndices: function() {
    return this.coordinateIndices;
  },

  /**
   * Get the encoding type of the layer.
   * @return {number} encoding type of the layer.
   */
  getEncodingType: function() {
    return this.encodingType;
  },

  /**
   * Get the image data of the layer.
   * @return {Object} image data of the layer.
   */
  getImageData: function() {
    return this.imageData;
  },

  /**
   * Set the line coordinates of the layer during IBRObject construction.
   * @param {List.<List.<number>>} lineCoordinates list of list of end point
    coordinates that each represent a line during rendering.
   */
  setLineCoordinates: function( lineCoordinates ) {
    this.lineCoordinates = lineCoordinates;
  },

  /**
   * Get the line coordinates of the layer.
   * @return {List.<List.<number>>} list of list of end point coordinates that
    each represent a line during rendering.
   */
  getLineCoordinates: function() {
    return this.lineCoordinates;
  },

} );

export {Layer};
