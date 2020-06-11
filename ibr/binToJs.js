/**
 * @fileoverview This file takes a binary wire format ibr file, decode the information and store data in sessionStorage for visualization use
 * @author shuanglihtk@google.com (Shuang Li)
 */

function swap32(val) {
    return ((val & 0xFF) << 24)
           | ((val & 0xFF00) << 8)
           | ((val >> 8) & 0xFF00)
           | ((val >> 24) & 0xFF);
}

function onFileLoad(event) {
    var deserializedData = InternalBuildingRepresentation.read(new Pbf(event.target.result));
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
    coords = decodedCoordsString.split(",");
    var decodedCoordsList = [];
    for (const coord of coords) {
        coordinate = coord.split(" ");
        if (coordinate.length === 2) {
            decodedCoordsList.push(coordinate);
        }
    }

    // Read multiple ranges from Visualization.coordinates array and store them in sessionStorage for visualization later
    var layerCoordinates = [];
    sessionStorage.setItem('numOfLines', coordsRange.length/2);
    for (var i = 0; i < coordsRange.length; i += 2) {
        layerCoordinates[i/2] = [];
        for (var x = coordsRange[i]; x < coordsRange[i+1]; x++) {
            layerCoordinates[i/2].push(decodedCoordsList[x]);
        }
        sessionStorage.setItem('layerCoordinates' + i/2, JSON.stringify(layerCoordinates[i/2]));
    }

    window.location.href = "visualization.html";
}

function onChooseFile(event, onLoadFileHandler) {
    if (typeof window.FileReader !== 'function')
        throw ("The file API isn't supported on this browser.");
    let input = event.target;
    if (!input)
        throw ("The browser does not properly implement the event object");
    if (!input.files)
        throw ("This browser does not support the `files` property of the file input.");
    if (!input.files[0])
        return undefined;
    let file = input.files[0];
    let fr = new FileReader();
    fr.onload = onLoadFileHandler;
    fr.readAsArrayBuffer(file);
}

