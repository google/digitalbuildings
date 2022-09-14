# ABEL
#### Automated Building Equipment Loader

## Overview
ABEL is a tool allowing systems integrators to easily and efficiently create [Building Configuration files](https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md) and [UDMI Site Models](https://github.com/faucetsdn/udmi/blob/master/docs/specs/site_model.md).

Previously, systems integrators had to a create a building configuration file by hand, but since building config is designed to be a machine=readable document, it is not human-friendly. The ABEL spreadsheet provides a frontend interface for gathering the informtion required to create a Building Config or a Site Model. ABEL also allows users to edit a Building Config file or UDMI Site Model by loading  either document into the frontend spreasheet and exporting it back out.

#### UDMI
ABEL does not yet support UDMI Site Model, but is planned to in the coming months.

## Setup and installation
Similar to the [GUID Generator](https://github.com/google/digitalbuildings/tree/master/tools/guid_generator), ABEL's setup process depends on the instance validator. It is best to run the global setup script to setup the entire tools library which ABEL depends on

1. Run: `git clone https://github.com/google/digitalbuildings.git`
2. Navigate to `DigitalBuildings/tools`
3. Depending on your operating system run either of the global setup scripts to configure dependencies
    * Windows: Run `pip_install.bat`
    * Unix: Run `sudo bash pip_install.sh`
5. Create a directory for ABEL to use at `~/abel/` and navigate to it
    * This will be used for storing authentication credentials and documents output from ABEL.
4. Obtain a spreadsheet token for your google sheets account
    1. You must be added to the `carson-eng-testing` service account on the `partner-db-api` gcp project
        * Contact someone to find out more about this
    2. Create a token request file at `~/abel/token_request.json` with contents:
        ```
        {"scope": [    "https://www.googleapis.com/auth/spreadsheets" ],  "lifetime": "3600s"}
        ```
    3. Run the below curl command to obtain a token:
        ```
            curl -X POST \
            -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
            -H "Content-Type: application/json; charset=utf-8" \
            -d @token_request.json \
            "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/carson-eng-testing@partner-db-api-test.iam.gserviceaccount.com:generateAccessToken" >| spreadsheet_token.json
        ```
    * `spreadsheet_token.json` should look something like:
        ```
        {
          "accessToken": "ya29.c.AXv0zTOa9p5K78GtGntoIQCqyt2R572qZ3…",
          "expireTime": "2022-02-24T19:57:26Z"
        }
        ```

## Using ABEL
The core functionality of ABEL is to:
* Ingest a ABEL spreadsheet and export a valid Building Config document
* Ingest a Building config and export an ABEL spreadsheet

#### Command-line arguments for ABEL:
* `-t / --token` (required) path to the GCP project token. The path should be ~/abel/token.json 
* `-s / --spreadsheet_id` (required) id for a google sheets spreadsheet. If necessary, create a blank spreadsheet. 
    * [Google Sheets Template](https://docs.google.com/spreadsheets/d/1qKMlpJI5-_h_8innNniEkpatMBcRHSGekrRwTsPQ618/edit#gid=455639674)

    * **MAKE SURE TO SHARE THE SPREADSHEET WITH THIS SERVICE ACCOUNT AS AN EDITOR**

    `carson-eng-testing@partner-db-api-test.iam.gserviceaccount.com`
    or the project id and service account bound to your previously generated token.
    
* `-b / --building_config` (optional) absolute path to a local building configuration file
    * [View a sample building config](https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md)
    
#### Spreadsheet -> Building Config
```
python3 abel.py -t absolute/path/to/token -s input_spreadsheet_id
```

#### Building Config -> Spreadsheet
```
python3 abel.py -t absolute/path/to/token -b absolute/path/to/building/config -s output_spreadsheet_id
```



## Notes
