import {BlockingGrid} from './BlockingGrid.js';
import {Visualization} from './Visualization.js';
import {swap32} from './util.js';

/**
 * Constructor of IBRObject Class.
 * @param {JSONObject} pbfDecodedJsonObject JSON decoded from input IBR file.
 */
function IBRObject(pbfDecodedJsonObject) {
  // Check if structure contains any boundary data
  if (pbfDecodedJsonObject.boundary === null) {
    this.hasBoundary = false;
  } else {
    this.hasBoundary = true;
    // Decode Indices from data.visualization[].coordinate_indices
    const boundaryList = pbfDecodedJsonObject.boundary;
    const boundaryBuffer = boundaryList.buffer.slice(
        boundaryList.byteOffset,
        boundaryList.byteOffset + boundaryList.length);
    const boundaryRange = new Uint32Array(boundaryBuffer);
    for (let i = 0; i < boundaryRange.length; i++) {
      boundaryRange[i] = swap32(boundaryRange[i]);
    }
    this.boundary = boundaryRange;
  }

  this.connections = pbfDecodedJsonObject.connections;

  this.externalReference = pbfDecodedJsonObject.external_reference;

  this.guid = pbfDecodedJsonObject.guid;

  this.metadata = pbfDecodedJsonObject.metadata;

  this.name = pbfDecodedJsonObject.name;

  this.structuralType = pbfDecodedJsonObject.structural_type;

  // Check if structure contains any coordinates lookup data
  if (pbfDecodedJsonObject.coordinates_lookup === null) {
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
    this.coordinates = Float32Array.from(coordsLookupList);
  }

  // format: Map.<visName{String}, visualizationData{Visualization}>
  this.visualizations = new Map();
  // Check if structure contains any visualization data
  if (pbfDecodedJsonObject.visualization.length === 0 ||
      (!this.hasCoordinatesLookup)) {
    this.hasVisualizations = false;
  } else {
    this.hasVisualizations = true;
    for (let i = 0; i < pbfDecodedJsonObject.visualization.length; i++) {
      this.visualizations.set(pbfDecodedJsonObject.visualization[i].id,
          new Visualization(pbfDecodedJsonObject.visualization[i],
              this.coordinates));
    }
  }

  // for datafiles that have top level name is ""
  if (pbfDecodedJsonObject.name === '' || pbfDecodedJsonObject.name === null) {
    this.name = 'ibrData.name';
  }

  this.subStructures = pbfDecodedJsonObject.structures;

  this.hasBlockingGrid = false;
  this.blockingGrid = pbfDecodedJsonObject.blocking_grid;
  if (pbfDecodedJsonObject.blocking_grid !== null &&
  this.hasCoordinatesLookup) {
    this.hasBlockingGrid = true;
    this.blockingGrid = new BlockingGrid(pbfDecodedJsonObject.blocking_grid,
        this.coordinates);
  }
}

Object.assign(IBRObject.prototype, {

  constructor: IBRObject,

  /**
   * Get the name of the IBRObject.
   * @return {String} name of the IBRObject.
   */
  getName: function() {
    return this.name;
  },

  /**
   * Get a list of names of the IBRObject visualizations.
   * @return {List.<String>} list of names of the IBRObject visualizations.
   */
  getVisualizationNames: function() {
    return Array.from(this.visualizations.keys());
  },

  /**
   * Get a visualization of the IBRObject based on given visualization ID.
   * @param {String} visualizationID ID of the visualization requested.
   * @return {Visualization} the visualization with the name visualizationID
    in IBRObject.
   */
  getVisualization: function(visualizationID) {
    return this.visualizations.get(visualizationID);
  },

  /**
   * Get a list of sub structures of the IBRObject.
   * @return {List.<Object>} list of sub structures of the IBRObject.
   */
  getSubStructures: function() {
    return this.subStructures;
  },

  /**
   * Get the structural type of the IBRObject.
   * @return {Number} structural type of the IBRObject.
   */
  getStructuralType: function() {
    return this.structuralType;
  },

  /**
   * Get a list of visualizations of the IBRObject.
   * @return {List.<Visualization>} list of visualizations of the IBRObject.
   */
  getVisualizations: function() {
    return this.visualizations;
  },

  /**
   * Get coordinates lookup.
   * @return {List.<Number>} coordinates lookup of the IBRObject.
   */
  getCoordinates: function() {
    return this.coordinates;
  },

  /**
   * Get blocking grid.
   * @return {BlockingGrid} Blocking grid of the IBRObject.
   */
  getBlockingGrid: function() {
    return this.blockingGrid;
  },

  /**
   * Convert IBRObject object to JSON format.
   * @return {JSONObject} json format of IBRObject object.
   */
  toJson: function() {
    const json = {};
    if (this.hasBlockingGrid) {
      json.blocking_grid = this.blockingGrid.toJson();
    } else {
      json.blocking_grid = null;
    }
    json.boundary = this.boundary;
    json.connections = this.connections;
    json.coordinates_lookup = null;
    if (this.hasCoordinatesLookup) {
      const tempCoordinates = this.coordinates;
      const coordsDV = new DataView(tempCoordinates.buffer);
      const coordsList = [];
      for (let i = 0; i < tempCoordinates.length; i += 1) {
        coordsList.push(coordsDV.getFloat32(i * 4, false));
      }
      json.coordinates_lookup = new Uint8Array(
          Float32Array.from(coordsList).buffer);
    }
    json.external_reference = this.externalReference;
    json.guid = this.guid;
    json.metadata = this.metadata;
    if (this.name === 'ibrData.name') {
      json.name = null;
    } else {
      json.name = this.name;
    }
    json.structural_type = this.structuralType;
    json.structures = [];
    if (this.subStructures.length != 0) {
      for (const struct of this.subStructures) {
        json.structures.push(new IBRObject(struct).toJson());
      }
    }
    json.visualization = [];
    for (const visualization of Array.from(this.visualizations.values())) {
      json.visualization.push(visualization.toJson());
    }
    return json;
  },

});
export {IBRObject};
