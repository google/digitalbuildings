# ABEL

ABEL is an acronym that stands for **A**utomated **B**uilding **E**ntity **L**oader. It is a tool that assists systems integrators (and other DBO users) in efficiently creating and
modifying [Building Configuration YAML files](../../ontology/docs/building_config.md).

ABEL has the following key features:
* Convert a Google Sheet (in the ABEL Spreadsheet Template) to a building configuration YAML file
  * Run Instance Validator (with optional telemetry validation) on the building configuration file
* Convert a building configuration YAML file to a Google Sheet

## Table of Contents

* [Setup and Installation](#setup-and-installation)
* [Using ABEL](#using-abel)
  * [Update Workflow](#update-workflow)
  * [Initialization Workflow](#initialization-workflow)
  * [Split Workflow](#split-workflow)

## Setup and Installation

Before starting the setup and installation process, please ensure that the dependencies are met:

1. You are running **Python 3.9** or higher

2. you have installed the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)

The total setup process should only take about 15 minutes. The process is broken into two parts:

1. Setup a virtual environment using [virtualenv](https://virtualenv.pypa.io/en/latest/) and install all of the
proper dependencies

2. Obtain credentials for [Google Sheets API](https://developers.google.com/sheets/api/reference/rest) for use with
ABEL

### Set up a tooling environment

If environment is already set up then the following steps can be ignored.

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
    ./pip_install.sh
    ```
  
  * Windows:
  
    ```
    pip_install.bat
    ```

6. Navigate to the [ABEL directory](./)

```
cd abel
```

### Obtain a GCP OAuth client credential

1. Contact your IoT Technical Program Manager and ask for an OAuth client `credential.json` file for authenticating against Google Sheets API.

2. Use the `credential.json` file for ABEL's `--credential` command line argument.

## Using ABEL
ABEL has a few pieces of core functionality, they are as follows:
1. Modify a spreadsheet or a building configuration for an existing building to produce an [UPDATE building config](../../ontology/docs/building_config.md#update)
    * [Update Workflow](#update-workflow)

2. Create a [Building Config](../../ontology/docs/building_config.md) from an [ABEL spreadsheet](../../tools/abel/validators/README.md) for a new building 
    * [Initialization Workflow](#initialization-workflow)

3. Split a building configuration file on a namespace
    * [Split Workflow](#split-workflow)

### Command-line arguments for ABEL
1. `-c` or `--credential` **Required**: The absolute or relative path to a GCP OAuth client credential file. An OAuth client credential is required for authentication against Google Sheets service.

2. `-s` or `--spreadsheet_id`: The ID associated with a Google Sheets spreadsheet
    * [ABEL Spreadsheet Template](https://docs.google.com/spreadsheets/d/1b6IRimNS1dAtPjkNN-fk4TirnLzOiDyyUmOKP_MhMM0/copy#gid=980240783)
    * A Google Sheets ID is found embedded into the spreadsheet's URL (e.g., `https://docs/google/com/spreadsheets/d/<spreadsheet_id>/edit#gid=123467`). Required when ABEL is creating a building configuration from a Google spreadsheet.

3. `-b` or `--building_config`: The absolute or relative path to a local building configuration file. Only required for the `Building Configuration -> Spreadsheet` workflow.
    * [Building Configuration Docs](../../ontology/docs/building_config.md)

4. `-p` or `--subscription` **[Optional]**: A fully-qualified path to a Google Cloud Pubsub subscription, e.g., `projects/google.com:your-project/subscriptions/your-subscription`. This parameter is only required for telemetry validation.

5. `-o` or `--timeout` **[Optional]**: Custom timeout duration in seconds for the telemetry validation test. The default value is 600 seconds, or 10 minutes. If this time limit is exceeded before the validator receives a test pubsub message for each of the entities configured in the given building configuration file, the test will fail with an error and report the entities that were not heard from.

6. `-m` or `--modified-types-filepath` **[Optional]**: A fully-qualified path to a modified ontology that is not in the [DigitalBuildings repository](../..). The [Ontology Validator](../validators/ontology_validator) will surface validation results from the modified ontology, and building configuration files will be validated against the modified ontology.

7. `-d` or `--output-dir`: An absolute or relative file path to a directory which ABEL can write files to. ABEL must have write access to this directory or else an error will be raised.

### The ABEL Spreadsheet
The ABEL spreadsheet serves as a user-friendly interface for ABEL and is what allows a user to make changes to machine-readable documents like [Building Config](../../ontology/docs/building_config.md).

Please see the [ABEL Spreadsheet docs](../../tools/abel/validators/README.md) for detailed instructions on how to create your own spreadsheet.

### Update Workflow

If you would like to create a building configuration to update an already onboarded building, there are two options:

Generate an ABEL spreadsheet from an exported building configuration.

  1. In `digitalbuildings/tools/abel` run ABEL with the command:

      ```
      python3 abel.py -c /path/to/credential.json -b absolute/path/to/building/config
      ```
To generate a building config from an already-updated spreadsheet.

  1. In `digitalbuildings/tools/abel` run ABEL with the command:

      ```
      python3 abel.py -s <input_spreadsheet_id> -c <path/to/client_credential.json> -d <path/to/output/directory>
      ```

  3. If your spreadsheet does not pass the validation criteria found in the
    [spreadsheet docs](../../tools/abel/validators/README.md) then ABEL will fast-fail and a validation report will be created in the current directory with the name `spreadsheet_validation_<todays_date_and_time>.log`

  4. The resulting building configuration file and instance validation report will be written to the current directory with the following names:
      * `bc_export_<today_date_and_time>.yaml`
      * `instance_validation_<today_date_and_time>.log`

### Initialization Workflow
If you would like create a building configuration file under the initialization operation

The process for using an ABEL spreadsheet to generate a new building configuration is as
follows:

1. Create a spreadsheet for ABEL from [ABEL Spreadsheet template](https://docs.google.com/spreadsheets/d/1nlFVwVvmumBSIAAAv7xq1-xuqGy0k1ONyrG2rMqrgdE/copy#gid=980240783)

2. Populate your spreadsheet. A well-defined guide on how to populate your
   spreadsheet can be found in the [spreadsheet docs](../../tools/abel/validators/README.md)

3. In `digitalbuildings/tools/abel` run ABEL with the command:
    ```
    python3 abel.py -s <input_spreadsheet_id> -c <path/to/client_credential.json> -d <path/to/output/directory>
    ```

4. Choose option 2: Create a spreadsheet for a new building

5. If your spreadsheet does not pass the validation criteria found in the [spreadsheet docs](../../tools/abel/validators/README.md) then ABEL will fast-fail and a validation report will be created in the directory specified with the `-d` arguments with the name `spreadsheet_validation_<todays_date_and_time>.log`

6. The resulting building configuration file and instance validation report will be written to the same directory with the following names:
   * `bc_export_<today_date_and_time>.yaml`
   * `instance_validation_<today_date_and_time>.log`

### Split Workflow
To split a building configuration file on a specific DBO namespace:

1. Run abel with a json credential and a building configuration:
    ```
    python3 abel.py -c </path/to/credential.json> -b </path/to/building/config>
    ```
2. Select option 3: `Split a building config`
  
4. ABEL will generate a new building configuration split on the desired namespace along with any dependencies (e.g., a building configuration containing only entities in the DBO `METERS` namespace).
     * Provide the `-d` argument if you would like ABEL to write to a specific directory.
