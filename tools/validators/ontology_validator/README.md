# Ontology Validator

The Ontology Validator allows users validate a local set of ontology YAML files (i.e., new ontology extensions or modifications) to ensure all extensions/modifications conform to DBO guidelines. Ontology Validator is also run on all pull requests that are opened within the DBO repository.

## Install requirements
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

### Install Packages

To install the requirements please run the following pip command:

1. Run `python3 -m pip install --upgrade pip` to ensure that your Python package management tools are up-to-date.
2. Run `python3 -m pip install .` from `digitalbuildings/tools/validators/ontology_validator`.


## Ontology Validator Workflow
The validator source code can be found [here](yamlformat/validator/validate_types.py).

The validator is Python-based and takes the following parameters:

* `--original` or `-o`: An absolute or relative path to the original files of the ontology.
* `--modified-ontology-types` or `-m` **[Optional]**: An absolute or relative path to the modified files of the ontology.
* `--interactive` or `-i` **[Optional]**: Enables interactive mode.

The validator can be run as follows: `python3 validator.py -o=Users/foo/ontology/` or `python3 validator.py --original=Users/foo/ontology/`

### Ontology Types Extended

If you have extended the ontology by adding new types to your local ontology, run the following: `python3 validator.py --original=Users/foo/ontology/ --modified-ontology-types=path/to/modified/ontology/types/folder`

When using a modified ontology, ensure you follow the folder-naming convention: `digitalbuildings/ontology/yaml`.

**Note:** as of the current development stage, you must clone the entire repository and run this ontology validator script from this directory.
