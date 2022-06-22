# Digital Buildings Toolkit

The Digital Buildings Toolkit provides a centralized
method for interfacing with all of the tools contained within the Digital
Buildings Repository. Currently, the toolkit only supports building configuration
instance validation and guid generation, but additional funcionality will be
implemented in the future.

## Setup

1. Follow setup instructions for the [Instance Validator](./validators/instance_validator).
2. Follow setup instructions for the [GUID Generator](./guid_generator).
3. Run `sudo python setup.py` for this directory.

## Toolkit Workflow

Run `python toolkit.py` and provide the following arguments:

1. `-i/--input` The absolute filepath of a building configuration file(.yaml).

2. `-m/--modified-types-filepath` **[Optional]** Validate entity types in the building configuration file against a modified ontology that is not in the main repository. Default is the [Digital Buildings Ontology](https://github.com/google/digitalbuildings/tree/master/ontology/yaml).

3. `-g/--generate` Generates GUIDs for entities in the building configuration file. Since the instance validator expects the [new building configuration format](https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#new-format), this option also converts a building configuration from the old format to the new format.

4. `-v/--validate` Runs instance validator to validate the building configuration file.

5. After a building configuration's entity types are validated, validation must also be run on the telemetry payload using:

  * `-s/--subscription` The fully-qualified path to a Google Cloud Pubsub subscription, e.g. projects/google.com:your-project/subscriptions/your-subscription.

  * `-a/--service-account` The fully-qualified path to a service account key file corresponding to an account that has permission to pull messages from the subscription.

  * `-t/--timeout` **[Optional]** The timeout duration in seconds for the telemetry validation test. The default value is 600 seconds, or 10 minutes. If this time limit is exceeded before the validator receives a test pubsub message for each of the entities configured in the given instance config file, the test will fail with an error and report the entities that were not heard from.

  * **NOTE:** The service account key and subscription are provided by the Google team. Please reach out to your IoT TPM for guidance.

6. `-r/--report-filename` To write results to a validation log.

For example:
`python toolkit.py -i //path/to/file -g -v -s subscription-name -a service-account-name -r //path/to/report`
1. Takes in a building configuration file.
2. Generates guids for every entity instance.
3. Re-writes building config in the new format.
4. Validates the building configuration.
5. Validates the telemetry payload.
6. Writes validation results to the report filepath.

**NOTE:** The new building configuration format switches entities being keyed by codes
to being keyed by guids, and Ids are removed. To convert from old format to the
new format, run your building configuration file(.yaml) through the [guid generator](https://github.com/google/digitalbuildings/tree/master/tools/guid_generator).
