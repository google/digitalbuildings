# Instance Validator

The Instance Validator allows validation of YAML instance files to make sure they conform to the given ontology model.

## Usage
The Instance Validator is written in Python3 and takes as an argument the path pointing to the instance files.

To use to ontology defined in this repository, run the validator as following: `python3 main.py --input path/to/YOUR_BUILDING_CONFIG.yaml`

If you want to use a modified ontology, run the following: `python3 main.py --input path/to/test_file.yaml --modified-ontology-types path/to/modified/ontology/types/folder`

Note: as of the current development stage, you must clone the entire repository and run this instance validator script from this directory.
