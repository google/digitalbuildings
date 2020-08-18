# Instance Validator

The Instance Validator allows validation of YAML instance files to make sure they conform to the given ontology model.

## Usage
The Instance Validator is written in Python3 and takes as an argument the path pointing to the instance files.

To use to ontology defined in this repository, run the validator as following: `python3 instance_validator.py --input path/to/YOUR_BUILDING_CONFIG.yaml`

### Ontology Types extended
In case of you extended the ontology by adding new types, run the following: `python3 instance_validator.py --input path/to/YOUR_BUILDING_CONFIG.yaml --modified-ontology-types path/to/modified/ontology/types/folder`

When using a modified ontology, ensure you follow the folder-naming convention: `digitalbuildings/ontology/yaml`. This will allow the instance validator to rely on the new types in the ontology.

Note: as of the current development stage, you must clone the entire repository and run this instance validator script from this directory.
