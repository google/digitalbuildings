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
1. You are running **Python 3.9** or higher
3. You have installed [virtualenv](https://pypi.org/project/virtualenv/)
2. you have installed the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)

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
  tooling\Scripts\activate
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

5. Navigate to the [ABEL directory](./)

```
cd abel
```

### Obtain a spreadsheet token for your google sheets account

1. [Initialize gcloud CLI](https://cloud.google.com/sdk/docs/initializing)
    1. Run `gcloud init`
    2. Choose option 1: `re-initialize default configuration`
    3. Choose option 2: Enter your Google credentials
    4. Choose option 1: Enter your GCP project id
    5. Don't configure a cloud region and zone
    6. Run `gcloud auth application-default login` to set your current login as your
       default configuration

![gcloud init screenshot](../../ontology/docs/figures/tools/gcloud_init.png?raw=true)

More info can be found in [gcloud docs on authorizing with the gcloud CLI](https://cloud.google.com/sdk/docs/authorizing)

2. Contact your IoT Technical Program Manager and ask to be added to a GCP service account.

3. Create a token request file, `token_request.json` with contents:

    ```
    {"scope": ["https://www.googleapis.com/auth/spreadsheets"],  "lifetime": "3600s"}
    ```

4. Send an http request to gcloud auth server to receive an access token:

* Linux/MacOS: Run the following curl command to obtain a token by replacing
   `<your-service-account>@<project-id>.iam.gserviceaccount.com` with your service
   account from step #1.

    ```
        curl -X POST -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) -H "Content-Type: application/json; charset=utf-8" -d @token_request.json "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/<your-service-account>@<project-id>.iam.gserviceaccount.com:generateAccessToken" >| spreadsheet_token.json
    ```
* Windows: Execute `get_token.bat` or run the following script in your command prompt:

    ```
    @echo off

    FOR /F "delims=" %i IN ('gcloud auth application-default print-access-t`oken') DO set token=%i
    SET header=Authorization: Bearer

    SET auth_token="%header%%token%"

    curl -X POST -H %auth_token% -H "Content-Type: application/json; charset=utf-8" -d @token_request.json "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/<your-service-account>@<project-id>.iam.gserviceaccount.com:generateAccessToken" > spreadsheet_token.json

    more spreadsheet_token.json
    ```

    Remember to replace
    `<your-service-account>@<project-id>.iam.gserviceaccount.com:generateAccessToken`
    with the service account from step #1 in either `get_token.bat` or the above
    script.

5. Confirm `spreadsheet_token.json` looks similar to:

    ```
    {
      "accessToken": "ya29.c...",
      "expireTime": "2022-02-24T19:57:26Z"
    }
    ```

 ***note:*** Spreadsheet tokens only last one hour and the command from step #3
 must be run again to generate a new token.

## Using ABEL
ABEL has a few pieces of core functionality, they are:
* Ingest an [ABEL spreadsheet](../../tools/abel/validators/README.md) and export a valid [Building Config](../../ontology/docs/building_config.md) file
* Ingest a [Building Config](../../ontology/docs/building_config.md) and export an [ABEL spreadsheet](../../tools/abel/validators/README.md)

### Command-line arguments for ABEL:
`-s` or `--spreadsheet_id` **required** id for a google sheets spreadsheet
  * [ABEL Spreadsheet Template](https://docs.google.com/spreadsheets/d/1b6IRimNS1dAtPjkNN-fk4TirnLzOiDyyUmOKP_MhMM0/copy?usp=sharing)
  * A Google Sheets ID is found embedded into the spreadsheet's url.
  e.g. `https://docs/google/com/spreadsheets/d/<spreadsheet_id>/edit#gid=123467`

`-b` or `--building_config` absolute path to a local building configuration
file. Only required for the `Building Config -> Spreadsheet` workflow.
  * [Building Configuration Docs](../../ontology/docs/building_config.md)

`-t` or `--token` path to the GCP project token. Default path for
  the token is the current directory, but an alternate relative or absolute path
  may be provided. Only required if the token is stored in a directory that isn't
  the current directory.

`-p` or `--subscription` fully-qualified path to a Google Cloud Pubsub subscription, e.g. `projects/google.com:your-project/subscriptions/your-subscription`. This parameter is only required for telemetry validation.

`-a` or `--service-account` path to a service account key file corresponding to an account that has permission to pull messages from the subscription. Optional for telemetry validation if gcloud default service account authentication is used.

`-o` or `--timeout` timeout duration in seconds for the telemetry validation test. The default value is 600 seconds, or 10 minutes. If this time limit is exceeded before the validator receives a test pubsub message for each of the entities configured in the given instance config file, the test will fail with an error and report the entities that were not heard from.

`-m` or `--modified-types-filepath` fully-qualified path to a modified ontology
that is not in the [DigitalBuildings repository](../..). The [Ontology
Validator](../validators/ontology_validator) will surface validation results
from the modified ontology, and Building Configuration files will be validated
against the modified ontology.

### The ABEL Spreadsheet
The ABEL spreadsheet serves as a user-friendly interface for ABEL and is what
allows a user to make changes to machine readable documents like [Building
Config](../../ontology/docs/building_config.md).

Please see the [ABEL spreadsheet docs](../../tools/abel/validators/README.md) for detailed instructions on how to create your own spreadsheet.

### Spreadsheet -> Building Config

The process for using an ABEL spreadsheet to generate a Building Config is as
follows:

1. Create a spreadsheet for ABEL from [ABEL Spreadsheet template](https://docs.google.com/spreadsheets/d/1tcLjFnHiXUT-xh5C1hRKiUVaUH_CzgSI8zFQ_B8q7vs/copy#gid=980240783)
2. Share your spreadsheet with your GCP service account and project id as an editor. Refer to Google Sheets documentation on [how to share a google sheet](https://support.google.com/docs/answer/9331169?hl=en#6.1).
3. Populate your spreadsheet. A well defined guide on how to populate your
   spreadsheet can be found in the [spreadsheet docs](../../tools/abel/validators/README.md)
4. In `digitalbuildings/tools/abel` run ABEL with the command:
```
python3 abel.py -s <input_spreadsheet_id>
```
5. If your spreadsheet does not pass the validation criteria found in the
   [spreadsheet docs](../../tools/abel/validators/README.md) then ABEL will fast
   fail and a validation
   report will be created in your current directory with the name,
   `spreadsheet_validation_<todays_date_and_time>.log`
6. The resulting Building Config and instance validation report will be written
   to the current directory with names:
   * `bc_export_<today_date_and_time>.yaml`
   * `instance_validation_<today_date_and_time>.log`

### Building Config -> Spreadsheet

The process for using a building config to generate an ABEL spreadsheet is as
follows:

1. Create a blank spreadsheet for ABEL to write to from [ABEL Spreadsheet template](https://docs.google.com/spreadsheets/d/1b6IRimNS1dAtPjkNN-fk4TirnLzOiDyyUmOKP_MhMM0/copy?usp=sharing)
2. Share your spreadsheet with your GCP service account and project id as an editor. Refer to Google Sheets documentation on [how to share a google sheet](https://support.google.com/docs/answer/9331169?hl=en#6.1).
3. In `digitalbuildings/tools/abel` run ABEL with the command:
```
python3 abel.py -b absolute/path/to/building/config -s <output_spreadsheet_id>
```
