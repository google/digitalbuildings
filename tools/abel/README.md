# ABEL
### Automated Building Entity Loader

## Overview
ABEL is a tool allowing system integrators to easily and efficiently create and modify [Building Configuration files](https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md).

## Setup and installation

### Setting up a tooling environment

Clone the Digital Buildings respository

  ```git clone https://github.com/google/digitalbuildings.git```

Navigate to the Digital Buildings Repository's tooling library

  ```cd digitalbuildings/tools/```

Create a virtual environment with an environment name, in this example: `tooling`

  ```virtualenv tooling```

Activate your virtual environment

* MacOs/Linux: `source tooling/bin/activate`

* Windows: `tooling/Scripts/activate`

Depending on your operating system run either of the global setup scripts to configure dependencies

* Linux/MacOs: `bash pip_install.sh`

* Windows: `pip_install.bat`

### Obtain a spreadsheet token for your google sheets account

1. Be added to a GCP service account with `Service Account User` and `Service Account Token Creator` roles.

    * Please contact your IoT TPM for details and to be added to a project.

2. Create a token request file, `token_request.json` with contents:

    ```
    {"scope": [    "https://www.googleapis.com/auth/spreadsheets" ],  "lifetime": "3600s"}
    ```

3. Run the below curl command to obtain a token:

    ```
        curl -X POST \
        -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
        -H "Content-Type: application/json; charset=utf-8" \
        -d @token_request.json \
        "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/your-service-account@project-id.iam.gserviceaccount.com:generateAccessToken" >| spreadsheet_token.json
    ```

4. `spreadsheet_token.json` should look something like:

    ```
    {
      "accessToken": "ya29.c.AXv0zTOa9p5K78GtGntoIQCqyt2R572qZ3…",
      "expireTime": "2022-02-24T19:57:26Z"
    }
    ```

## The ABEL Spreadsheet
The ABEL spreadsheet serves as a frontend for ABEL.

Please see the [ABEL spreadsheet docs](./validators/README.md) for detailed instructions on how to use the spreadsheet.

## Using ABEL
The core functionality of ABEL is to:
* Ingest a ABEL spreadsheet and export a valid Building Config document
* Ingest a Building config and export an ABEL spreadsheet

### Command-line arguments for ABEL:
`-s` or `--spreadsheet_id` (required) id for a google sheets spreadsheet.
  * [Google Sheets Template](https://docs.google.com/spreadsheets/d/1qKMlpJI5-_h_8innNniEkpatMBcRHSGekrRwTsPQ618/copy#gid=980240783)

  * **MAKE SURE TO SHARE THE SPREADSHEET WITH YOUR SERVICE ACCOUNT AND PROJECT ID AS AN EDITOR**
  * Refer to Google Sheets documentation on [how to share a google sheet](https://support.google.com/docs/answer/9331169?hl=en#6.1)

`-b` or `--building_config` (optional) absolute path to a local building configuration file
  * [View a sample building config](https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md)

`-t` or `--token` (optional) path to the GCP project token. Default path for
  the token is the current directory, but an alternate relative or absolute path
  may be provided.
    
### Spreadsheet -> Building Config
```
python3 abel.py -s <input_spreadsheet_id>
```

### Building Config -> Spreadsheet
```
python3 abel.py -b absolute/path/to/building/config -s <output_spreadsheet_id>
```
