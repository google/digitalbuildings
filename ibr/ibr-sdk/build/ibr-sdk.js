/**
 * @fileoverview This file contains functions that render given ibr binary data to (array of) THREE objects that can be used in browser.
 * @author shuanglihtk@google.com (Shuang Li)
 */

(function (global, factory) {
	typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports) :
	typeof define === 'function' && define.amd ? define(['exports'], factory) :
	(global = global || self, factory(global.IBRSDK = {}));
}(this, (function (exports) { 'use strict';

    /**
     * Converts raw ibr visualization data into three.js Line objects.
     * @param {Byte} data Binary data read directly from .ibr file
     * @return {Array.<Line>} lines List of three.js Line objects generated from input ibr data
     */
    function renderLayer(data) {

        var deserializedData = InternalBuildingRepresentation.read(new Pbf(data));
        var coordsIndexList = deserializedData.visualization[0].coordinates;
        var coordsRangeBuffer = coordsIndexList.buffer.slice(coordsIndexList.byteOffset, coordsIndexList.buffer.byteLength);
        var coordsRange = new Uint32Array(coordsRangeBuffer);
        for (var i = 0; i < coordsRange.length; i++) {
            coordsRange[i] = swap32(coordsRange[i]);
        }


        // Decode Coordinates from data.coordinatesLookup.encodedData
        var decoder = new TextDecoder('utf8');
        var decodedCoordsString = atob(decoder.decode(deserializedData.coordinates_lookup.encoded_data));

        // Put coordinates in data structure
        var coords = decodedCoordsString.split(",");
        var decodedCoordsList = [];
        for (const coord of coords) {
            var coordinate = coord.split(" ");
            if (coordinate.length === 2) {
                decodedCoordsList.push(coordinate);
            }
        }

        // Read multiple ranges from Visualization.coordinates array and store them in sessionStorage for visualization later
        var layerCoordinates = [];
        for (var i = 0; i < coordsRange.length; i += 2) {
            layerCoordinates[i/2] = [];
            for (var x = coordsRange[i]; x < coordsRange[i+1]; x++) {
                layerCoordinates[i/2].push(decodedCoordsList[x]);
            }
        }

        // Importing uploaded data
        var material1 = new THREE.LineBasicMaterial( { color: 0x0000ff } );
        var points = [], lines = [];
        var geometry, line;
        for (const layer of layerCoordinates) {
            for (const coordinate of layer) {
                points.push( new THREE.Vector3( coordinate[0], coordinate[1], 0 ) );
            }
            geometry = new THREE.BufferGeometry().setFromPoints( points );
            line = new THREE.LineLoop( geometry, material1 );
            lines.push( line );
        }
        return lines;
    }
    exports.renderLayer = renderLayer;

    Object.defineProperty(exports, '__esModule', { value: true });
})));