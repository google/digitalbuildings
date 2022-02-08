# Instance Validator

The Instance Validator allows validation of YAML instance files to make sure they conform to the given ontology model.

## Install

Installing and using the Instance Validator requires Python 3.7, and the specific Python command to run may vary depending on your operating system and the presence of Python 2. Use the appropriate command listed below when the instructions call for `python3`:

* MacOS & Linux: `python3`
* Windows (with only Python 3 installed): `python` or `py -3`
* Windows (with Python 2 and 3 installed): `py -3`

You can run the command with just the version flag (e.g. `python --version`) to verify that the result is `Python 3.*`.

1. Run `python3 -m pip install --upgrade pip setuptools` to ensure that your Python package management tools are up-to-date.
2. Run `python3 setup.py install` from digitalbuildings/tools/validators/ontology_validator.
3. Run `python3 setup.py install` from digitalbuildings/tools/validators/instance_validator.

## Usage

Navigate to digitalbuildings/tools/validators/instance_validator and run `python3 instance_validator.py --input path/to/YOUR_BUILDING_CONFIG.yaml` to validate your input file using the ontology defined in this repository.

To validate multiple input files at the same time, you can provide the `--input` parameter multiple times. (`-i` will also work).

You may also validate a directory, multiple directories, or any combination of directories and files using the `--input` flag. For example, the following is valid: 
`python instance_validator.py --input path/to/a/directory --input path/to/another/directory --input path/to/a/specific/file.yaml`

Note, however, that the directories must be mutually exclusive. Do not pass in a directory and one of its sub-directories, otherwise you will get an error. 

If the optional `--report-filename` parameter is provided, the validation results will be written to this report file. Otherwise, the results will be written to stdout.

### Ontology Types extended

If you have extended the ontology by adding new types to your local ontology, run the following: `python3 instance_validator.py --input path/to/YOUR_BUILDING_CONFIG.yaml --modified-ontology-types path/to/modified/ontology/types/folder`

When using a modified ontology, ensure you follow the folder-naming convention: `digitalbuildings/ontology/yaml`. This will allow the instance validator to rely on the new types in the ontology.

Note: as of the current development stage, you must clone the entire repository and run this instance validator script from this directory.

### Telemetry validation

The validator supports a telemetry validation mode. When this mode is enabled, the validator will listen on a provided pubsub subscription for telemetry messages, and validate the message contents against the instance configuration. It is recommended that you first use the instance validator with telemetry validation mode disabled, and then enable it after that passes.

If you would like to use the telemetry validation mode, you must provide the "--subscription" and "--service-account" parameters when running instance_validator.py. Failure to provide both of these parameters will result in early termination of the validator and an error message. If you do not provide either parameter, the validator will run with telemetry validation mode disabled.

The --subscription parameter value should be a fully-qualified path to a Google Cloud Pubsub subscription, e.g. projects/google.com:your-project/subscriptions/your-subscription.

The --service-account parameter value should be a path to a service account key file corresponding to an account that has permission to pull messages from the subscription.
To download the service account key, please follow the instructions provided [here](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys)

Optional parameter for the telemetry validation mode are:

--timeout: The timeout duration in seconds for the telemetry validation test. The default value is 600 seconds, or 10 minutes. If this time limit is exceeded before the validator receives a test pubsub message for each of the entities configured in the given instance config file, the test will fail with an error and report the entities that were not heard from.

--report-filename: If provided, errors from the telemetry validation test will be written to this report file. Otherwise, errors will be written to stdout.
