# IBR Javascript SDK

This purpose of this project is to allow developers to seemlessly work with CAD-like building data. This library allows users to seamlessly work with ibr data in javascript as well as provides built in methods to create a simple UI built on [THREE.js](https://github.com/mrdoob/three.js/)

## Instructions for Running the IBR UI:

1. Open terminal and build the sdk package:

```
cd digitalbuildings/ibr/ibr-sdk
`npm run build
```

2. Start a local server in python

`cd ..; python3 -m http.server`.

3. Navigate to http://0.0.0.0:8000/examples/html/

## Potential Issues and Fix

1. When using Chrome browser, see error "Blocked by CORS policy : Cross origin requests are only supported for protocol schemes: http, data, chrome, chrome-extension, https" in console