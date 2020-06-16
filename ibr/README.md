# Instructions for running the IBR UI:
1. Open terminal and run following commands:
    - `cd digitalbuildings/ibr`
    - `npm i ibr-sdk`
    - `mkdir -p temp/ && node_modules/.bin/pbf ibr.proto --browser > temp/ibr_pb_browser.js`
2. Open html/index.html in your browser
3. Click on "Choose File" button to open your ibr data file
##### Developer Note: 
*The ibr-sdk npm package is not published, hence it cannot yet be installed in other projects.*