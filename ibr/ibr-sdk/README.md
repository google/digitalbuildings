## Instructions for Running the IBR UI:

1. Open terminal and run following commands:
	- change directory to current directory: `cd digitalbuildings/ibr/ibr-sdk`
	- build production code from source: `npm run build`

2. Open html/index.html in your browser.

On Mac, start chrome from terminal using this command instead:
    - `open -a "Google Chrome" html/index.html --args --allow-file-access-from-files`

3. Navigate to localhost:8000/html

## Potential Issues and Fix

1. When using Chrome browser, see error "Blocked by CORS policy : Cross origin requests are only supported for protocol schemes: http, data, chrome, chrome-extension, https" in console

2. Start a local server in python
    - Open your command prompt (Windows)/ terminal (macOS/ Linux). To check Python is installed, enter the following command: `python -V`.
    - If python is installed, you should see a version number. If not, go to [python.org]() and install python3.
    - Once python3 is installed, run command `python3 -m http.server`.
    - Then navigate to http://0.0.0.0:8000/html/ in your browser.

3. Click on "Choose File" button to open your ibr data file
