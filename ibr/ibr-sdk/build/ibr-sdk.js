/**
 * @fileoverview This file contains functions that render given ibr binary data to (array of) THREE objects that can be used in browser.
 * @author shuanglihtk@google.com (Shuang Li)
 */

const TWOPOINTS = 6;

(function (global, factory) {
	typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports) :
	typeof define === 'function' && define.amd ? define(['exports'], factory) :
	(global = global || self, factory(global.IBRSDK = {}));
}(this, (function (exports) { 'use strict';

    /**
     * Swap endianness of 32bit numbers.
     */
    function swap32(val) {
        return ((val & 0xFF) << 24)
               | ((val & 0xFF00) << 8)
               | ((val >> 8) & 0xFF00)
               | ((val >> 24) & 0xFF);
    }

    /**
     * Converts raw ibr visualization data into three.js Line objects.
     * @param {Byte} data Binary data read directly from .ibr file
     * @return {Array.<Line>} lines List of three.js Line objects generated from input ibr data
     */
    function renderLayer(data) {

        // Decode Indices from data.visualization[].coordinate_indices
        var deserializedData = InternalBuildingRepresentation.read(new Pbf(data));
        var coordsIndexList, coordsRangeBuffer, coordsRange;
        var coordsRangeList = [];
        for (const visLayer of deserializedData.visualization) {
            coordsIndexList = visLayer.coordinate_indices;
            coordsRangeBuffer = coordsIndexList.buffer.slice(coordsIndexList.byteOffset, coordsIndexList.byteOffset+coordsIndexList.length);
            coordsRange = new Uint32Array(coordsRangeBuffer);
            for (var i = 0; i < coordsRange.length; i++) {
                coordsRange[i] = swap32(coordsRange[i]);
            }
            coordsRangeList.push(coordsRange);
        }

        // Decode Coordinates from data.coordinates_lookup
        var coordsLookup = deserializedData.coordinates_lookup;
        var coordsLookupBuffer = coordsLookup.buffer.slice(coordsLookup.byteOffset, coordsLookup.byteOffset+coordsLookup.length);
        var coordsLookupDV = new DataView(coordsLookupBuffer);
        var coordsLookupList = [];
        for (var i = 0; i < coordsLookup.length/4; i+=4) {
            coordsLookupList.push(coordsLookupDV.getFloat32(i, false));
        }

        // Read multiple ranges from Visualization.coordinates array and store them in sessionStorage for visualization later
        var layerCoordinates = [], layerPH = [], coordsLine = [];
        for (const coordsRangeItem of coordsRangeList) {
            layerPH = [];
            for (var i = 0; i < coordsRangeItem.length; i+=2) {
                coordsLine = [];
                for (var j = coordsRangeItem[i]; j <= coordsRangeItem[i+1]; j+=3) {
                    coordsLine.push(coordsLookupList[j]);
                    coordsLine.push(coordsLookupList[j+1]);
                    coordsLine.push(coordsLookupList[j+2]);
                }
                layerPH.push(coordsLine);
            }
            layerCoordinates.push(layerPH);
        }

        // Render data into three.js objects
        var materials1 = new THREE.LineBasicMaterial( { color: 0xff0000 } );
        var materials = [new THREE.LineBasicMaterial( { color: 0x00ffff } )];
        for (var i = 0; i < deserializedData.visualization.length-1; i++) {
            materials.push(materials1);
        }
        var lineLoopPoints = [], lineSegmentPoints = [], lineSegments = [], objects = [];
        var geometry, geometries;
        for (var i = 0; i < layerCoordinates.length; i++) {
            lineSegments = [];
            for (const line of layerCoordinates[i]) {
                lineSegmentPoints = [];
                lineLoopPoints = [];
                if (line.length === TWOPOINTS) {
                    for (var j = 0; j < line.length; j+=3) {
                        lineSegmentPoints.push( new THREE.Vector3( line[j], line[j+1], line[j+2] ) );
                    }
                    geometry = new THREE.BufferGeometry().setFromPoints( lineSegmentPoints );
                    lineSegments.push( geometry );
                } else {
                    for (var j = 0; j < line.length; j+=3) {
                        lineLoopPoints.push( new THREE.Vector3( line[j], line[j+1], line[j+2] ) );
                    }
                    geometry = new THREE.BufferGeometry().setFromPoints( lineLoopPoints );
                    objects.push( new THREE.LineLoop( geometry, materials[i] ) );
                }
            }
            if (lineSegments.length > 0) {
                geometries = THREE.BufferGeometryUtils.mergeBufferGeometries( lineSegments );
                objects.push( new THREE.LineSegments( geometries, materials[i] ) );
            }
        }

        return objects;
    }
    exports.renderLayer = renderLayer;

    Object.defineProperty(exports, '__esModule', { value: true });
})));