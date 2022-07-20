# Instance Validator

The Instance Validator allows validation of YAML instance files to make sure they conform to the given ontology model.

## Install

Installing and using the Instance Validator requires Python 3.9, and the specific Python command to run may vary depending on your operating system and the presence of Python 2. Use the appropriate command listed below when the instructions call for `python3`:

* MacOS & Linux: `python3`
* Windows (with only Python 3 installed): `python` or `py -3`
* Windows (with Python 2 and 3 installed): `py -3`

You can run the command with just the version flag (e.g. `python --version`) to verify that the result is `Python 3.*`.

1. Run `python3 -m pip install --upgrade pip setuptools` to ensure that your Python package management tools are up-to-date.
2. Run `python3 setup.py install` from digitalbuildings/tools/validators/ontology_validator.
3. Run `python3 setup.py install` from digitalbuildings/tools/validators/instance_validator.

## Usage

Navigate to digitalbuildings/tools/validators/instance_validator and run `python3 instance_validator.py --input path/to/YOUR_BUILDING_CONFIG.yaml` to validate your input file using the ontology defined in this repository.

To validate multiple input files at the same time, you can provide the "`-i/--input` parameter multiple times.

If the optional `-r/--report-filename` parameter is provided, the validation results will be written to this report file. Otherwise, the results will be written to stdout.

### Ontology Types extended

If you have extended the ontology by adding new types to your local ontology, run the following: `python3 instance_validator.py --input path/to/YOUR_BUILDING_CONFIG.yaml --modified-ontology-types path/to/modified/ontology/types/folder`

When using a modified ontology, ensure you follow the folder-naming convention: `digitalbuildings/ontology/yaml`. This will allow the instance validator to rely on the new types in the ontology.

Note: as of the current development stage, you must clone the entire repository and run this instance validator script from this directory.

### Telemetry validation

The validator supports a telemetry validation mode. When this mode is enabled, the validator will listen on a provided pubsub subscription for telemetry messages, and validate the message contents against the instance configuration. It is recommended that you first use the instance validator with telemetry validation mode disabled, and then enable it after that passes.

If you would like to use the telemetry validation mode, you must provide the `--subscription` parameter, and you must either be authentication with [gcloud application-default credentials](https://cloud.google.com/sdk/gcloud/reference/auth/application-default) with an account which has adequate permissions to access the given subscription, or provide a `--service-account` parameter when running instance_validator.py. Failure to provide both of these parameters will result in early termination of the validator and an error message. If you do not provide either parameter, the validator will run with telemetry validation mode disabled.
**NOTE** The service account key and subscription are provided by the Google team. Please reach out to your IoT TPM for guidance.

The `--subscription parameter` value should be a fully-qualified path to a Google Cloud Pubsub subscription, e.g. projects/google.com:your-project/subscriptions/your-subscription.

Optional parameter for the telemetry validation mode are:

The `--service-account` parameter value should be a path to a service account key file corresponding to an account that has permission to pull messages from the subscription.

`--timeout`: The timeout duration in seconds for the telemetry validation test. The default value is 600 seconds, or 10 minutes. If this time limit is exceeded before the validator receives a test pubsub message for each of the entities configured in the given instance config file, the test will fail with an error and report the entities that were not heard from.

`--report-filename`: If provided, errors from the telemetry validation test will be written to this report file. Otherwise, errors will be written to stdout.

### Instance Validator Workflow

Run `python instance_validator.py` and provide the following arguments:

1. `-i/--input` The absolute filepath of a building configuration file(.yaml).

2. `-m/--modified-types-filepath` **[Optional]** Validate entity types in the building configuration file against a modified ontology that is not in the main repository. Default is the [Digital Buildings Ontology](https://github.com/google/digitalbuildings/tree/master/ontology/yaml).

3. After a building configuration's entity types are validated, validation must also be run on the telemetry payload using:

  * `-s/--subscription` The fully-qualified path to a Google Cloud Pubsub subscription, e.g. projects/google.com:your-project/subscriptions/your-subscription.

  * `-a/--service-account` The fully-qualified path to a service account key file corresponding to an account that has permission to pull messages from the subscription.

  * `-t/--timeout` **[Optional]** The timeout duration in seconds for the telemetry validation test. The default value is 600 seconds, or 10 minutes. If this time limit is exceeded before the validator receives a test pubsub message for each of the entities configured in the given instance config file, the test will fail with an error and report the entities that were not heard from.

  * **NOTE:** The service account key and subscription are provided by the Google team. Please reach out to your IoT TPM for guidance.

4. `-r/--report-filename` To write results to a validation log.

For example:
`python instance_validator.py.py -i //path/to/file -s subscription-name -a service-account-name -r //path/to/report`
1. Takes in an building configuration file.
4. Validates the building configuration.
3. Validates telemetry payload.
5. Writes validation results to the report filepath.

**NOTE:** The new Building Config format switches entities being keyed by codes
to being keyed by guids and Ids are removed. To convert the old format to the
new format, run your config.yaml through the [guid generator](https://github.com/google/digitalbuildings/tree/master/tools/guid_generator).

### Warnings and Errors

The Instance Validator has two types of outputs, **Warnings** and **Errors**. In short, errors are exposed when a Building Config is not readable by the instance validator while warnings are exposed when a Building Config is readable but
its contents may not be valid.

**Errors** cause the validator to exit prematurely with some kind of exception. For example, An error could be caused by an entity block not containing a `GUID`. This would raise an exception in the
validation logic and cause the validator to exit prematurely because the instance validator expects every entity block in a Building Config to have an associated `GUID`, either as a key or an entity block element. The [guid generator](https://github.com/google/digitalbuildings/tree/master/tools/guid_generator) must be used to generate guids for a Building Configuration file. Other entity block elements are `type` and `code`.

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

**Warnings** on the other hand expose inconsistencies in the content of an entity block but do not cause the validator to fail since the core elements of what make an entity block readable are still present. For example, if the fields defined in `translation` or `links` do not align with the fields for the entity's type as defined in [Digital Builings Ontology](https://github.com/google/digitalbuildings/tree/master/ontology/yaml), then the validator will warn the user it is not a valid entity.

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

