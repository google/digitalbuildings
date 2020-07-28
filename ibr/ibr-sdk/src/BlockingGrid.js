import {Visualization} from './Visualization.js';

/**
 * Constructor of BlockingGrid Class.
 * @param {JSONObject} pbfDecodedJsonObject JSON decoded from input IBR file.
 * @param {List.<Number>} coordsLookup Coords Lookup from the parent structure.
 */
function BlockingGrid(pbfDecodedJsonObject, coordsLookup) {
  this.id = pbfDecodedJsonObject.id;

  // Check if structure contains any visualization data
  if (pbfDecodedJsonObject.visualization === null) {
    this.hasVisualizations = false;
  } else {
    this.hasVisualizations = true;
    this.visualization =
        new Visualization(pbfDecodedJsonObject.visualization, coordsLookup);
  }
}

Object.assign(BlockingGrid.prototype, {

  constructor: BlockingGrid,

  /**
   * Get the ID of the BlockingGrid.
   * @return {String} name of the BlockingGrid.
   */
  getID: function() {
    return this.id;
  },

  /**
   * Get the visualization of the BlockingGrid Object.
   * @return {Visualization} visualization of the BlockingGrid Object.
   */
  getVisualization: function() {
    return this.visualization;
  },

  toJson: function() {
    const json = {};
    json.id = this.id;
    json.visualization = this.visualization.toJson();
    return json;
  },

});
export {BlockingGrid};
