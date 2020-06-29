# Internal Building Representation (IBR) File Format
IBR implements single file format that can be adapted to multiple use cases in any building.

Data in different verticals such as spatial, assets, and ontology often come from different source systems. This presents a challenge when a developer wants ensure updated data in downstream systems, especially when they want to combine data across multiple verticals. IBR is a solution that allows all of it to be combined in a meaningful, portable way.

IBR has no opinion of data requirements. If a developer wants to use IBR as an asset tracking tool, they can utilize the Objects message. If they later want to map asset locations to a single floor, that is possible by including a Layers message while updating the Objects messages with location data. If they want to track assets with relation to specific space classes, then they can add that data at a later stage without making a breaking change.

IBR comes with a rendering library built on THREE.js that can be used to easily create a custom UI to visualize and edit the compact data. This allows developers to build custom features and have more control over their tooling. 

## Instructions for running the IBR UI:
1. Open terminal and run following commands:
    - `cd digitalbuildings/ibr`
    - `npm i ibr-sdk`
    - `mkdir -p temp/ && node_modules/.bin/pbf ibr.proto --browser > temp/ibr_pb_browser.js`
2. Open html/index.html in your browser
3. Click on "Choose File" button to open your ibr data file
##### Developer Note: 
*The ibr-sdk npm package is not published, hence it cannot yet be installed in other projects.*
