/**
 * @fileoverview This file contains functions that render given ibr binary data to (array of) THREE objects.
 * @author shuanglihtk@google.com (Shuang Li)
 */

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
    var materials = [new THREE.LineBasicMaterial( { color: 0x00ffff } ), new THREE.LineBasicMaterial( { color: 0xff0000 } )];
    var points = [], lines = [];
    var geometry, line;
    for (var i = 0; i < layerCoordinates.length; i++) {
        for (const l of layerCoordinates[i]) {
            points = [];
            for (var j = 0; j < l.length; j+=3) {
                points.push( new THREE.Vector3( l[j], l[j+1], l[j+2] ) );
            }
            geometry = new THREE.BufferGeometry().setFromPoints( points );
            line = new THREE.LineLoop( geometry, materials[i] );
            lines.push( line );
        }
    }
    return lines;
}

export { renderLayer };