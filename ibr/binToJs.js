/**
 * @fileoverview This file takes a binary wire format ibr file, decode the information and store data in sessionStorage for visualization use
 * @author Shuang Li
 */

function onFileLoad(event) {
    var deserializedData = InternalBuildingRepresentation.read(new Pbf(event.target.result));
    var coordsIndexList = deserializedData.visualization[0].coordinates.coordinate_index;

    // Decode Coordinates from data.coordinatesLookup.encodedData
    var decoder = new TextDecoder('utf8');
    var decodedCoordsString = atob(decoder.decode(deserializedData.coordinates_lookup.encoded_data));

    // Put coordinates in data structure
    coords = decodedCoordsString.split(",");
    var decodedCoordsList = [];
    for (x in coords){
        coordinate = coords[x].split(" ");
        if (coordinate.length === 2){
            decodedCoordsList.push(coordinate);
        }
    }

    // Generate data to be visualized
    var layerCoordinates = [];
    for (x in coordsIndexList){
        layerCoordinates.push(decodedCoordsList[coordsIndexList[x]])
    }

    sessionStorage.setItem('layerCoordinates', JSON.stringify(layerCoordinates));

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

