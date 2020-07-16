import { Layer } from './Layer.js';

/**
 * Constructor of IBRObject Class.
 * @param {Objecy} pbfDecodedJsonObject JSON Object decoded using Pbf library
 from raw ibr binary data.
 */
function IBRObject( pbfDecodedJsonObject ) {
  // format: Map.<layerName{String}, layerData{Layer}>
  this.layers = new Map();
  // Check if structure contains any visualization data
  if ( pbfDecodedJsonObject.visualization.length === 0) {
    this.hasLayers = false;
  } else {
    this.hasLayers = true;
    for ( let i = 0; i < pbfDecodedJsonObject.visualization.length; i++) {
      this.layers.set(pbfDecodedJsonObject.visualization[i].id,
          new Layer(pbfDecodedJsonObject.visualization[i]));
    }
  }

  // Check if structure contains any coordinates lookup data
  if (pbfDecodedJsonObject.coordinates_lookup == null) {
    this.hasCoordinatesLookup = false;
  } else {
    this.hasCoordinatesLookup = true;
    // Decode Coordinates from data.coordinates_lookup
    const coordsLookup = pbfDecodedJsonObject.coordinates_lookup;
    const coordsLookupBuffer = coordsLookup.buffer.slice(
        coordsLookup.byteOffset, coordsLookup.byteOffset +
        coordsLookup.length);
    const coordsLookupDV = new DataView(coordsLookupBuffer);
    const coordsLookupList = [];
    for (let i = 0; i < coordsLookup.length; i += 4) {
      coordsLookupList.push(coordsLookupDV.getFloat32(i, false));
    }
    this.coordinates = coordsLookupList;
  }

  this.name = pbfDecodedJsonObject.name;
  // for datafiles that have top level name is ""
  if (pbfDecodedJsonObject.name === '' || pbfDecodedJsonObject.name == null) {
    this.name = 'ibrData.name';
  }

  this.subStructures = pbfDecodedJsonObject.structures;
}

Object.assign( IBRObject.prototype, {

  constructor: IBRObject,

  /**
   * Get the name of the IBRObject.
   * @return {String} name of the IBRObject.
   */
  getName: function() {
    return this.name;
  },

  /**
   * Get a list of names of the IBRObject layers.
   * @return {List.<String>} list of names of the IBRObject layers.
   */
  getLayerNames: function() {
    return Array.from( this.layers.keys() );
  },

  /**
   * Get a layer of the IBRObject based on given layer ID.
   * @param {String} layerID ID of the layer requested.
   * @return {Layer} the layer with the name layerID in IBRObject.
   */
  getLayer: function( layerID ) {
    return this.layers.get( layerID );
  },

  /**
   * Get a list of sub structures of the IBRObject.
   * @return {List.<Object>} list of sub structures of the IBRObject.
   */
  getSubStructures: function() {
    return this.subStructures;
  },

  /**
   * Get a list of layers of the IBRObject.
   * @return {List.<Layer>} list of layers of the IBRObject.
   */
  getLayers: function() {
    return this.layers;
  },

  /**
   * Get coordinates lookup.
   * @return {List.<Number>} coordinates lookup of the IBRObject.
   */
  getCoordinates: function() {
    return this.coordinates;
  },

} );
export {IBRObject};
