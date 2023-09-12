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

2. Navigate to the [DigitalBuildings tooling library](../../tools/)

  ```
  cd digitalbuildings/tools/
  ```

3. Create a virtual environment with an environment name, in this example: `tooling`

  ```
  python3 -m venv tooling
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

### Obtain a GCP OAuth client credential

1. Contact your IoT Technical Program Manager and ask for an oauth client `credential.json` file for authenticating against Google Sheets API.

2. Use the `credential.json` file for ABEL's `--credential` command line argument.

## Using ABEL
ABEL has a few pieces of core functionality, they are:
1. Modify a spreadsheet or a building config for an existing building to produce an [UPDATE building config](../../ontology/docs/building_config.md#update)
  * [Update Workflow](#update-workflow)
2. Create a [Building Config](../../ontology/docs/building_config.md) from an [ABEL spreadsheet](../../tools/abel/validators/README.md) for a new building 
  * [Initialization workflow](#initialization-workflow)

### Command-line arguments for ABEL:
`-c` or `--credential` absolute or relative path to a gcp OAuth client
credential file. An OAuth client credential is required for authentication
against Google Sheets service.

`-s` or `--spreadsheet_id` id for a google sheets spreadsheet
  * [ABEL Spreadsheet Template](https://docs.google.com/spreadsheets/d/1b6IRimNS1dAtPjkNN-fk4TirnLzOiDyyUmOKP_MhMM0/copy#gid=980240783)
  * A Google Sheets ID is found embedded into the spreadsheet's url. Required when ABEL is creating a building config from a Google spreadsheet.
  e.g. `https://docs/google/com/spreadsheets/d/<spreadsheet_id>/edit#gid=123467`

`-b` or `--building_config` absolute o relative path to a local building configuration
file. Only required for the `Building Config -> Spreadsheet` workflow.
  * [Building Configuration Docs](../../ontology/docs/building_config.md)

`-p` or `--subscription` fully-qualified path to a Google Cloud Pubsub subscription, e.g. `projects/google.com:your-project/subscriptions/your-subscription`. This parameter is only required for telemetry validation.

`-o` or `--timeout` timeout duration in seconds for the telemetry validation test. The default value is 600 seconds, or 10 minutes. If this time limit is exceeded before the validator receives a test pubsub message for each of the entities configured in the given instance config file, the test will fail with an error and report the entities that were not heard from.

`-m` or `--modified-types-filepath` fully-qualified path to a modified ontology
that is not in the [DigitalBuildings repository](../..). The [Ontology
Validator](../validators/ontology_validator) will surface validation results
from the modified ontology, and Building Configuration files will be validated
against the modified ontology.

`-d` or `--output-dir` fully qualified or relative file path to a directory which ABEL can write validation logs to. ABEL must have write access to this directory or else an error will be raised.

### The ABEL Spreadsheet
The ABEL spreadsheet serves as a user-friendly interface for ABEL and is what
allows a user to make changes to machine readable documents like [Building
Config](../../ontology/docs/building_config.md).

Please see the [ABEL spreadsheet docs](../../tools/abel/validators/README.md) for detailed instructions on how to create your own spreadsheet.

### Update Workflow

If you would like to create a building config to update an already onboarded building, then there are two options:
1. Update an exported building config.

  The process for using a building config to generate an ABEL spreadsheet is as
  follows:

  1. In `digitalbuildings/tools/abel` run ABEL with the command:
  ```
  python3 abel.py -c /path/to/credential.json -b absolute/path/to/building/config
  ```

2. Generate a building config from an already updated spreadsheet.

  1. In `digitalbuildings/tools/abel` run ABEL with the command:
  ```
  python3 abel.py -s <input_spreadsheet_id> -c <path/to/client_credential.json> -d <path/to/output/directory>
  ```
  2. If your spreadsheet does not pass the validation criteria found in the
    [spreadsheet docs](../../tools/abel/validators/README.md) then ABEL will fast
    fail and a validation
    report will be created in your current directory with the name,
    `spreadsheet_validation_<todays_date_and_time>.log`
  3. The resulting Building Config and instance validation report will be written
    to the current directory with names:
    * `bc_export_<today_date_and_time>.yaml`
    * `instance_validation_<today_date_and_time>.log`

### Initialization workflow
If you would like create a building configuration file under the initialization operation

The process for using an ABEL spreadsheet to generate a new Building Config is as
follows:

1. Create a spreadsheet for ABEL from [ABEL Spreadsheet template](https://docs.google.com/spreadsheets/d/1tcLjFnHiXUT-xh5C1hRKiUVaUH_CzgSI8zFQ_B8q7vs/copy#gid=980240783)
2. Populate your spreadsheet. A well defined guide on how to populate your
   spreadsheet can be found in the [spreadsheet docs](../../tools/abel/validators/README.md)
3. In `digitalbuildings/tools/abel` run ABEL with the command:
```
python3 abel.py -s <input_spreadsheet_id> -c <path/to/client_credential.json> -d <path/to/output/directory>
```
4. If your spreadsheet does not pass the validation criteria found in the
   [spreadsheet docs](../../tools/abel/validators/README.md) then ABEL will fast
   fail and a validation report will be created in the directory specified with the `-d` arguments with the name,
   `spreadsheet_validation_<todays_date_and_time>.log`
5. The resulting Building Config and instance validation report will be written
   to the same directory with names:
   * `bc_export_<today_date_and_time>.yaml`
   * `instance_validation_<today_date_and_time>.log`
