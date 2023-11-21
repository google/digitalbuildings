# Digital Buildings Tools

Various tools have been developed to support the use of the Digital Buildings Ontology and Building Configuration files. 

The tools and their functions are summarized below:
  * [ABEL](./abel/README.md) generates from/to Google spreadsheet/[Building Configuration](../ontology/docs/building_config.md).
  * [Explorer](./explorer/README.md) allows users to explorer the ontology types and their associated fields.
  * [Instance Validator](./validators/instance_validator/README.md) allows users to validate a concrete instance of the ontology (i.e., a building configuration file).
    * A sub-function of the Instance Validator is to also [validate telemetry messages](./validators/instance_validator/README.md#telemetry-validation) 
    corresponding to entity blocks in a building configuration file.
  * [Ontology Validator](./validators/ontology_validator/README.md) allows users to validate a local version of the YAML ontology upon a change or an extension.

## Digital Buildings Toolkit

The Digital Buildings Toolkit provides a centralized method for interfacing with all of the tools contained within the Digital Buildings Repository.

### Toolkit Web Application

The [web-based toolkit application](dbo-toolkit-app.azurewebsites.net) also exists to provide a user-friendly interface to all of the Digital Buildings tools. 
**Note:** Curently, the Toolkit Web Application only supports the Instance Validatr. The team plans to support other tools in the near future.

### Install

To install please follow the instructions below.

#### Create a Virtual Environment

First, create a virtual environment with `venv` followed by the environment name (in this example: `tooling`) in the digitalbuildings repository.

```
python -m venv tooling
```


#### Activate the virtual environment

Mac OS / Linux:
```
source tooling/bin/activate
```

Windows
```
tooling\Scripts\activate
```

Then, you can either use pip or setuptools (to be deprecated).

#### Pip
1. Run the following command to ensure that your Python package management tools are up-to-date.

```
python3 -m pip install --upgrade pip
```

2. Run `bash pip_install.sh` or `pip_install.bat` (windows) from the following directory: `digitalbuildings/tools`.

#### Docker (Optional)

1. Install [Docker Desktop](https://docs.docker.com/desktop/)
2. Run `./tools/docker_run.sh` to build the docker image.
3. All tools can now be called by passing the tool name and arguments to `./tools/docker_run.sh`, for example, to run ABEL:
```
$ ./tools/docker_run.sh abel
```

#### Setup (to be deprecated)

1. Follow setup instructions for the [Instance Validator](./validators/instance_validator).
2. Follow setup instructions for the [GUID Generator](./guid_generator).
3. Run `sudo python setup.py` for this directory.

### Toolkit Workflow

Run `python toolkit.py` and provide the following arguments:

1. `--input` or `-i`: The absolute filepath of a building configuration file(.yaml).

2. `--modified-types-filepath` or `-m` **[Optional]**: Validates entity types in the building configuration file against a modified ontology (i.e., a local branch) that is not in the main repository. Default is the [Digital Buildings Ontology](https://github.com/google/digitalbuildings/tree/master/ontology/yaml).

3. `--generate` or `-g`: Generates GUIDs for entities in the building configuration file. Since the instance validator expects the [new building configuration format](https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#new-format), this option also converts a building configuration from the old format to the new format.

4. `--validate` or `-v`: Runs instance validator to validate the building configuration file.

5. After a building configuration's entity types are validated, validation must also be run on the telemetry payload using the following parameters:

  * `--subscription` or `-s`: The fully-qualified path to a Google Cloud Pubsub subscription (e.g., `projects/google.com:your-project/subscriptions/your-subscription`).

  * `--credential` or `-c`: An absolute or relative path to an OAuth client credential JSON file.

  * `--timeout` or `-t` **[Optional]**: The timeout duration in seconds for the telemetry validation test. The default value is 600 seconds, or 10 minutes. If this time limit is exceeded before the validator receives a test pubsub message for each of the entities configured in the given instance config file, the test will fail with an error and report the entities that were not heard from.

  * `--udmi` **[Optional]**: Validates entity metadata as [UDMI](https://github.com/faucetsdn/udmi/). Flag is set to `True` by default; change this parameter to `--udmi=False` when not validating against UDMI.

  * **NOTE:** The OAuth credential and subscription are provided by the Google team. Please reach out to your IoT TPM for guidance.

6. `--report-directory` or `-d`: To write instance validation (instance_validation_report.txt) and telemetry validation (telemetry_validation_report.json) reports to the `report-directory`; otherwise writes instance validation to console and telemetry validation to the current working directory.

For example, the following input

```
python toolkit.py -i //path/to/building/configuration/file.yaml -g -v -s subscription-name -c //path/to/oauth/cred.json -d //path/to/report-directory
```

results in these actions:
1. Ingests a building configuration file.
2. Generates guids for every entity instance in the buiding configuration file.
3. Re-writes building configuration file in the new format.
4. Validates the building configuration file.
5. Validates the telemetry payloads for each reporting entity in the building configuration file.
6. Writes validation results to the report directory as `//path/to/report-directory/instance_validation_report.txt` and `//path/to/report-directory/telemetry_validation_report.json` for instance validation and telemetry validation, respectfully.

**NOTE:** The new building configuration format requires that entities are keyed by Version 4 UUIDs (referred to as guids) instead of the code. To convert from old format to the new format, run your building configuration file(.yaml) through the [guid generator](https://github.com/google/digitalbuildings/tree/master/tools/guid_generator).

Any questions or concerns can be emailed to **BOS-GPS@google.com**.
