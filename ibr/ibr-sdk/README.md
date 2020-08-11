## Instructions for Running the IBR UI:

1. Open terminal and run following commands:
	- change directory to current directory: `cd digitalbuildings/ibr/ibr-sdk`
	- build production code from source: `npm run build`

2. Start a local server in python
   - Open your command prompt (Windows)/ terminal (macOS/ Linux). To check Python is installed, enter the following command: `python -V`.
   - If python is installed, you should see a version number. If not, go to [python.org](python.org) and install python3.
   - Once python3 is installed, change directory to include example folder using `cd ..`, then run command `python3 -m http.server`.

3. Navigate to http://0.0.0.0:8000/examples/html/

## Potential Issues and Fix

1. When using Chrome browser, see error "Blocked by CORS policy : Cross origin requests are only supported for protocol schemes: http, data, chrome, chrome-extension, https" in console

2. Click on "Choose File" button to open your ibr data file
