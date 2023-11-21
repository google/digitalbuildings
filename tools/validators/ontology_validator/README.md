# Ontology Validator

The Ontology Validator allows users validate a local set of ontology YAML files (i.e., new ontology extensions or modifications) to ensure all extensions/modifications conform to DBO guidelines. Ontology Validator is also run on all pull requests that are opened within the DBO repository.

## Install requirements

### First create a virtual env

Create the virtual environment with `virtualenv` followed by the environment name, in this example: `tooling`

```
virtualenv tooling
```


Activate the virtual environment

Mac OS / Linux:
```
source tooling/bin/activate
```

Windows
```
tooling\Scripts\activate
```

### Install the validator

To install the requirements please run the following pip command:

1. Run `python3 -m pip install --upgrade pip` to ensure that your Python package management tools are up-to-date.
2. Run `python3 -m pip install .` from digitalbuildings/tools/validators/ontology_validator.


## YAML Validator
The validator source code can be found [here](yamlformat/validator/validate_types.py).

The validator is Python-based and takes the following parameters:

* `-o/--original`: An absolute or relative path to the original files of the
  ontology.
* `-m/--modified-ontology-types` **[Optional]**: An absolute or relative path to the modified files of the ontology.
* `-i/--interactive`: Enables interactive mode.

The validator can be run as follows: `python3 validator.py -o=Users/foo/ontology/` or `python3 validator.py --original=Users/foo/ontology/`

### Ontology Types Extended

If you have extended the ontology by adding new types to your local ontology, run the following: `python3 validator.py --input path/to/YOUR_BUILDING_CONFIG.yaml --modified-ontology-types path/to/modified/ontology/types/folder`

When using a modified ontology, ensure you follow the folder-naming convention: `digitalbuildings/ontology/yaml`.

**Note:** as of the current development stage, you must clone the entire repository and run this ontology validator script from this directory.
