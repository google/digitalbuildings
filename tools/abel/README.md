# ABEL
### Automated Building Entity Loader

Allows system integrators to easily and efficiently create and
modify [Building Configuration files](../../ontology/docs/building_config.md).

## Setup and installation

The setup process is broken into two parts:

1. Setup a virtual environment using [virtualenv](https://virtualenv.pypa.io/en/latest/) and install all of the
proper dependencies
2. Obtain credentials for [Google Sheets API](https://developers.google.com/sheets/api/reference/rest) for use with
ABEL

Total setup process should only take about 15 minutes.

Before starting the setup and installation process, please ensure that the
dependencies are met:
1. You are running **python 3.9** or higher
3. You have installed [virtualenv](https://pypi.org/project/virtualenv/)
2. you have installed the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)
4. [Initialize the gcloud cli](https://cloud.google.com/sdk/docs/initializing)

### Set up a tooling environment

1. Clone the Digital Buildings repository

  ```
  git clone https://github.com/google/digitalbuildings.git
  ```

2. Navigate to the [digitalbuildings tooling library](../../tools/)

  ```
  cd digitalbuildings/tools/
  ```

3. Create a virtual environment with an environment name, in this example: `tooling`

  ```
  virtualenv tooling
  ```

4. Activate your virtual environment

* MacOs/Linux:

  ```
  source tooling/bin/activate
  ```

* Windows:

  ```
  tooling/Scripts/activate
  ```

5. Depending on your operating system, run either of the global setup scripts to configure dependencies

* Linux/MacOs:
  ```
  bash pip_install.sh
  ```

* Windows:

  ```
  pip_install.bat
  ```

### Obtain a spreadsheet token for your google sheets account

1. Contact your IoT Technical Program Manager and ask to be added to a GCP service account.

2. Create a token request file, `token_request.json` with contents:

    ```
    {"scope": [    "https://www.googleapis.com/auth/spreadsheets" ],  "lifetime": "3600s"}
    ```

3. Run the below curl command to obtain a token modifying the command with your
   service account from step #1. This command uses a dummy service account,
   `your-service-account@project-id.iam.gserviceaccount.com`

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

 ***note:*** spreadsheet tokens only last one hour and the command from step #3
 must be run again to generate a new token.

## The ABEL Spreadsheet
The ABEL spreadsheet serves as a user-friendly interface for ABEL and is what
allows a user to make changes to machine readable documents like [Building
Config](../../ontology/docs/building_config.md).

Please see the [ABEL spreadsheet docs](../../tools/abel/validators/README.md) for detailed instructions on how to use the spreadsheet.

## Using ABEL
ABEL has a few pieces of core functionality, they are:
* Ingest an [ABEL spreadsheet](https://docs.google.com/spreadsheets/d/1qKMlpJI5-_h_8innNniEkpatMBcRHSGekrRwTsPQ618/copy#gid=980240783) and export a valid [Building Config](../../ontology/docs/building_config.md) file.
* Ingest a [Building Config](../../ontology/docs/building_config.md) and export an ABEL spreadsheet.

### Command-line arguments for ABEL:
`-s` or `--spreadsheet_id` (required) id for a google sheets spreadsheet
  * [ABEL Spreadsheet Template](https://docs.google.com/spreadsheets/d/1qKMlpJI5-_h_8innNniEkpatMBcRHSGekrRwTsPQ618/copy#gid=980240783)
  * A Google Sheets ID is found embedded into the spreadsheet's url.
  e.g. `https://docs/google/com/spreadsheets/d/<spreadsheet_id>/edit#gid=123467`

`-b` or `--building_config` (optional) absolute path to a local building configuration file
  * [Building Configuration Docs](../../ontology/docs/building_config.md)

`-t` or `--token` (optional) path to the GCP project token. Default path for
  the token is the current directory, but an alternate relative or absolute path
  may be provided.

### Spreadsheet -> Building Config

The process for using an ABEL spreadsheet to generate a Building Config is as
follows:

1. Create a spreadsheet for ABEL from [ABEL Spreadsheet template](https://docs.google.com/spreadsheets/d/1tcLjFnHiXUT-xh5C1hRKiUVaUH_CzgSI8zFQ_B8q7vs/copy#gid=980240783)
2. Share your spreadsheet with your GCP service account and project id as an editor. Refer to Google Sheets documentation on [how to share a google sheet](https://support.google.com/docs/answer/9331169?hl=en#6.1).
3. Populate your spreadsheet. A well defined guide on how to populate your
   spreadsheet can be found in the [spreadsheet docs](../../tools/abel/validators/README.md)
4. Run ABEL with the command:
```
python3 abel.py -s <input_spreadsheet_id>
```
5. If your spreadsheet does not pass the validation criteria found in the
   [spreadsheet docs](../../tools/abel/validators/README.md) then ABEL will fast
   fail and `a validation
   report will be created in your current directory with the name,
   `spreadsheet_validation_<todays_date_and_time>.yaml`
6. The resulting Building Config and instance validation report will be written
   to the current directory with names:
   * `bc_export_<today_date_and_time>.yaml`
   * `instance_validation_<today_date_and_time>.txt`

### Building Config -> Spreadsheet

The process for using a building config to generate an ABEL spreadsheet is as
follows:

1. Create a blank spreadsheet for ABEL to write to from [ABEL Spreadsheet template](https://docs.google.com/spreadsheets/d/1tcLjFnHiXUT-xh5C1hRKiUVaUH_CzgSI8zFQ_B8q7vs/copy#gid=980240783)
2. Share your spreadsheet with your GCP service account and project id as an editor. Refer to Google Sheets documentation on [how to share a google sheet](https://support.google.com/docs/answer/9331169?hl=en#6.1).
3. Run ABEL with the command:
```
python3 abel.py -b absolute/path/to/building/config -s <output_spreadsheet_id>
```
