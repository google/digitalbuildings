# Instance Validator

The Instance Validator allows validation of concrete DBO instances (i.e., building configuration files) to ensure they conform to the given ontology model, are formatted correctly, and contain all required fields. There is also optional functionality to validate telemetry messages for all reporting entities in the building configuration using Telemetry Validator.

## Install

Installing and using the Instance Validator requires Python 3.9, and the specific Python command to run may vary depending on your operating system and the presence of Python 2. Use the appropriate command listed below when the instructions call for `python3`:

* MacOS & Linux: `python3`
* Windows (with only Python 3 installed): `python` or `py -3`
* Windows (with Python 3 installed): `py -3`

You can run the command with just the version flag (e.g. `python --version`) to verify that the result is `Python 3.*`.

### Create a Virtual Environment

First, create a virtual environment with `venv` followed by the environment name (in this example: `tooling`) in the digitalbuildings repository.

```
python -m venv tooling
```


### Activate the Virtual Environment

Mac OS / Linux:
```
source tooling/bin/activate
```

Windows
```
tooling\Scripts\activate
```
## Install Packages
Next, you can either use pip or setuptools (to be deprecated) to install the necessary packages and dependencies.

### Install Pip
1. Run the following command to ensure that your Python package management tools are up-to-date.

```
python3 -m pip install --upgrade pip
```

2. Run `bash pip_install.sh` (MacOS / Linux) or `pip_install.bat` (Windows) from the following directory: `digitalbuildings/tools`.

### Setuptools (to be deprecated)

1. Run `python3 -m pip install --upgrade pip setuptools` to ensure that your Python package management tools are up-to-date.
2. Run `python3 setup.py install` from the following directory: digitalbuildings/tools/validators/ontology_validator.
3. Run `python3 setup.py install` from the following directory: digitalbuildings/tools/validators/instance_validator.

## Instance Validator Workflow

Navigate to `digitalbuildings/tools/validators/instance_validator` and run `python instance_validator.py` with the following parameters:

1. `--input` or `-i`: The absolute filepath of a building configuration file(.yaml). To validate multiple input files at the same time, you can provide the `-input` parameter multiple times.

2. `--modified-types-filepath` or `-m` **[Optional]**: Validate entity types in the building configuration file against a modified ontology that is not in the main repository. Default is the [Digital Buildings Ontology](https://github.com/google/digitalbuildings/tree/master/ontology/yaml).
    * When using a modified ontology, ensure you follow the folder-naming convention: `digitalbuildings/ontology/yaml`. This will allow the instance validator to rely on the new types in the ontology.
    * **Note:** as of the current development stage, you must clone the entire repository and run this instance validator script from this directory.

3. `--report-filename` or `-r` **[Optional]**: Writes instance validation results to the specified report file. Otherwise, the results will be written to stdout.

4. `--report-directory` or `-d` **[Optional]**: Writes instance validation (instance_validation_report.txt) and telemetry validation (telemetry_validation_report.json) reports to the specified `report-directory`. By default, writes instance validation output to the console and telemetry validation output to the current working directory.

5. `--udmi` **[Optional]**: Validates entity metadata as [UDMI](https://github.com/faucetsdn/udmi/). Flag is set to `True` by default; change this parameter to `--udmi=False` when not validating against UDMI.

### Telemetry Validation

The validator supports a telemetry validation mode. When this mode is enabled, the validator will listen on a provided pubsub subscription for telemetry messages, and validate the message contents against the instance configuration. **It is recommended that you first use the instance validator with telemetry validation mode disabled, and then enable it after that passes.**

If you would like to use the telemetry validation mode, you must provide the `--subscription` parameter and the `--credential` parameter. **NOTE:** The OAuth credential and subscription are provided by the Google team. Please reach out to your IoT TPM for guidance. If a GCP Oauth client credential is not provided, then application default credentials will be used to authenticate against Google APIs. Running telemetry validation will also output a machine-readable log of the validation performed on a set of devices. This log will be output as `telemetry_validation_log.json` in the current working directory, unless otherwise specefied using the `--report_directory` parameter.

1. `--credential` or `-c`: An absolute or relative path to an OAuth client credential JSON file.

2. `--subscription` or `-s`: The fully-qualified path to a Google Cloud Pubsub subscription (e.g., `projects/google.com:your-project/subscriptions/your-subscription`).

3. `--timeout` or `-t` **[Optional]**: The timeout duration in seconds for the telemetry validation test. The default value is 600 seconds, or 10 minutes. If this time limit is exceeded before the validator receives a test pubsub message for each of the entities configured in the given instance config file, the test will fail with an error and report the entities that were not heard from.

For example, the following input
```
python instance_validator.py.py -i //path/to/file -s subscription-name -c //path/to/client/cred.json -d //path/to/report-directory
```
results in these actions:
1. Ingests a building configuration file.
2. Validates the building configuration file with the instance validator (using the default ontology master brach).
3. Validates the telemetry payloads for each reporting entity in the building configuration file.
4. Writes instance and telemetry validation results to the report directory as `//path/to/report-directory/instance_validation_report.txt` and `//path/to/report-directory/telemetry_validation_report.json`.

**NOTE:** The new building configuration format requires that entities are keyed by Version 4 UUIDs (referred to as guids) instead of the code. To convert from old format to the new format, run your building configuration file(.yaml) through the [guid generator](https://github.com/google/digitalbuildings/tree/master/tools/guid_generator).

### Warnings and Errors

The Instance Validator has two types of outputs: **Warnings** and **Errors**. In short, errors are exposed when a Building Config is not readable by the instance validator while warnings are exposed when a Building Config is readable but its contents may not be valid.

#### Errors
Errors cause the validator to exit prematurely with some kind of exception. For example, An error could be caused by an entity block not containing a `GUID`. This would raise an exception in the validation logic and cause the validator to exit prematurely because the instance validator expects every entity block in a Building Config to have an associated `GUID`. The [GUID generator](https://github.com/google/digitalbuildings/tree/master/tools/guid_generator) must be used to generate GUIDs for a Building Configuration file. Other entity block elements are `type` and `code`.

    The following entity block would throw an error because it does not contain a type nor a code.

    8318f346-10b4-44f0-ac0b-bf7659510bfa:
      translation:
        zone_air_temperature_sensor:
          present_value: "temp_1"
          units:
            key: "units"
            values:
              degrees_celsius: "degC"
              degrees_fahrenheit: "degF"

#### Warnings
Warnings, on the other hand, expose inconsistencies in the content of an entity block but do not cause the validator to fail since the core elements of what make an entity block readable are still present. For example, if the fields defined in `translation` or `links` do not align with the fields for the entity's type as defined in [Digital Buildings Ontology](https://github.com/google/digitalbuildings/tree/master/ontology/yaml), then the validator will warn the user it is not a valid entity.

    The following entity block would only expose a warning because these are not the fields for VAV_SD_DSP as defined in DBO:

    4931e096-dea5-4b81-86ad-234c6d07b978:
      code: VAV-2
      connections:
        c773b86d-b0c0-46fc-bd3f-d726fadd5f1e:
        - FEEDS
      links:
        547a33c5-0ce4-4dfb-9924-5169a3475c89:
          supply_air_flowrate_sensor: supply_air_flowrate_sensor_2
        2b152e08-3440-4358-9067-3f2acc58c982:
          zone_air_temperature_sensor: zone_air_temperature_sensor
          zone_air_temperature_setpoint: zone_air_temperature_setpoint
      type: HVAC/VAV_SD_CSP

