/**
 * @fileoverview This file contains functions that render given ibr binary data to (array of) THREE objects that can be used in browser.
 * @author shuanglihtk@google.com (Shuang Li)
 */

// the length of one 3D coordinates (x, y, z) in the coordinate lookup float array
const ONE_POINT = 3;
// the length of two 3D coordinates (x, y, z) in the coordinate lookup float array
const TWO_POINTS = 6;

(function (global, factory) {
	typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports) :
	typeof define === 'function' && define.amd ? define(['exports'], factory) :
	(global = global || self, factory(global.IBRSDK = {}));
}(this, (function (exports) {
    'use strict';

    /**
     * Decode raw ibr data into structures.
     * @param {Byte} data Binary data read directly from .ibr file
     * @return {Array.<Object>} structures List of structure objects generated from input ibr data
     */
    function unpackStructure(data) {
        var deserializedData = InternalBuildingRepresentation.read(new Pbf(data));
        var structures = [];
        structures.push( deserializedData );
        if ( deserializedData.structures.length > 0 ) {
            structures = deserializedData.structures;
        }
        return structures;
    }

    /**
     * Swap endianness of 32bit numbers.
     */
    function swap32(val) {
        return ((val & 0xFF) << 24)
               | ((val & 0xFF00) << 8)
               | ((val >> 8) & 0xFF00)
               | ((val >> 24) & 0xFF);
    }

    // List of colors from jquery.color.js plugin
    var Colors = {};
    Colors.names = ["#00ffff",
        "#f0ffff",
        "#f5f5dc",
        "#000000",
        "#0000ff",
        "#a52a2a",
        "#00ffff",
        "#00008b",
        "#008b8b",
        "#a9a9a9",
        "#006400",
        "#bdb76b",
        "#8b008b",
        "#556b2f",
        "#ff8c00",
        "#9932cc",
        "#8b0000",
        "#e9967a",
        "#9400d3",
        "#ff00ff",
        "#ffd700",
        "#008000",
        "#4b0082",
        "#f0e68c",
        "#add8e6",
        "#e0ffff",
        "#90ee90",
        "#d3d3d3",
        "#ffb6c1",
        "#ffffe0",
        "#00ff00",
        "#ff00ff",
        "#800000",
        "#000080",
        "#808000",
        "#ffa500",
        "#ffc0cb",
        "#800080",
        "#800080",
        "#ff0000",
        "#c0c0c0",
        "#ffffff",
        "#ffff00"
    ];

    Colors.random = function() {
        var result = this.names[Math.floor( Math.random() * (this.names.length - 1) )];
        return result;
    };

    /**
     * Converts decoded ibr structure data into three.js Line objects.
     * @param {Object} structure structures decoded from raw ibr data
     * @return {Array.<Line>} lines List of three.js Line objects generated from input ibr data
     */
    function renderLayer(structure) {

        // Decode Indices from data.visualization[].coordinate_indices
        var coordsIndexList, coordsRangeBuffer, coordsRange;
        var coordsRangeList = [];
        for (const visLayer of structure.visualization) {
            coordsIndexList = visLayer.coordinate_indices;
            coordsRangeBuffer = coordsIndexList.buffer.slice(coordsIndexList.byteOffset, coordsIndexList.byteOffset+coordsIndexList.length);
            coordsRange = new Uint32Array(coordsRangeBuffer);
            for (var i = 0; i < coordsRange.length; i++) {
                coordsRange[i] = swap32(coordsRange[i]);
            }
            coordsRangeList.push(coordsRange);
        }

        // Decode Coordinates from data.coordinates_lookup
        var coordsLookup = structure.coordinates_lookup;
        var coordsLookupBuffer = coordsLookup.buffer.slice(coordsLookup.byteOffset, coordsLookup.byteOffset+coordsLookup.length);
        var coordsLookupDV = new DataView(coordsLookupBuffer);
        var coordsLookupList = [];
        for (var i = 0; i < coordsLookup.length/4; i+=4) {
            coordsLookupList.push(coordsLookupDV.getFloat32(i, false));
        }

        // Read multiple ranges from Visualization.coordinates array and store them in sessionStorage for visualization later
        var layerCoordinates = [];
        for (const coordsRangeItem of coordsRangeList) {
            var layerPH = [];
            for (var i = 0; i < coordsRangeItem.length; i+=2) {
                var coordsLine = [];
                for (var j = coordsRangeItem[i]; j <= coordsRangeItem[i+1]; j+=ONE_POINT) {
                    coordsLine.push(coordsLookupList[j]);
                    coordsLine.push(coordsLookupList[j+1]);
                    coordsLine.push(coordsLookupList[j+2]);
                }
                layerPH.push(coordsLine);
            }
            layerCoordinates.push(layerPH);
        }

        // Render data into three.js objects
        var materials = [];
        for (var i = 0; i < structure.visualization.length-1; i++) {
            materials.push(new THREE.LineBasicMaterial( { color: Colors.random() } ));
        }
        var objects = [];
        for (var i = 0; i < layerCoordinates.length; i++) {
            var lineSegments = [];
            for (const line of layerCoordinates[i]) {
                var linePoints = [];
                for (var j = 0; j < line.length; j+=ONE_POINT) {
                    linePoints.push( new THREE.Vector3( line[j], line[j+1], line[j+2] ) );
                }
                var geometry = new THREE.BufferGeometry().setFromPoints( linePoints );
                if (line.length === TWO_POINTS) {
                    lineSegments.push( geometry ); // group geometries for performance reason
                } else {
                    objects.push( new THREE.LineLoop( geometry, materials[i] ) );
                }
            }
            if (lineSegments.length > 0) {
                var geometries = THREE.BufferGeometryUtils.mergeBufferGeometries( lineSegments );
                objects.push( new THREE.LineSegments( geometries, materials[i] ) );
            }
        }
        return objects;
    }

    exports.renderLayer = renderLayer;
    exports.unpackStructure = unpackStructure;

    Object.defineProperty(exports, '__esModule', { value: true });
})));