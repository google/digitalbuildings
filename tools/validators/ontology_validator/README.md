# Validator

The Ontology Validator allows you to extend the ontology and then validate it to make sure it is comform to guidelines.

## Install requirements

To install the requirements please run the following pip command:

1. Run `python3 -m pip install --upgrade pip` to ensure that your Python package management tools are up-to-date.
2. Run `python3 -m pip install -r requirements.txt ` from digitalbuildings/tools/validators/ontology_validator.


## Yaml Validator
The validator source code can be found [here](yamlformat/validator/validate_types.py).

The Validator is python based, it takes the following arguments:

* original `-o` or `--original`: a path pointing to the original files of the
  ontology.
* modified-type-filepath (optional) `-m` or `--modified-ontology-types`:
  a path pointing to the modified files of the ontology.
* interactive `-i` or `--interactive`:enables interactive mode.

The validator can be run as following: `python3 validator.py
-o=Users/foo/ontology/` or `python3 validator.py --original=Users/foo/ontology/`

### Ontology Types extended

If you have extended the ontology by adding new types to your local ontology, run the following: `python3 validator.py --input path/to/YOUR_BUILDING_CONFIG.yaml --modified-ontology-types path/to/modified/ontology/types/folder`

When using a modified ontology, ensure you follow the folder-naming convention: `digitalbuildings/ontology/yaml`.

Note: as of the current development stage, you must clone the entire repository and run this ontology validator script from this directory.
