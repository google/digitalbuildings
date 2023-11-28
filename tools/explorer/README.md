# Ontology Explorer

The Ontology explorer allows a user to ask a few basic questions of the ontology:
* What fields are associated with a type name?
* What are the types associated with a given set of fields?
* Is a field defined within a certain namespace?

## Install

To install please follow the instructions below.

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
Next, you can either use pip or setup (to be deprecated) to install the necessary packages and dependencies.

#### Pip
1. Run the following command to ensure that your Python package management tools are up-to-date.

```
python3 -m pip install --upgrade pip
```

2. Run `python3 -m pip install .` from the following directories:

* digitalbuildings/tools/validators/ontology_validator
* digitalbuildings/tools/validators/instance_validator
* digitalbuildings/tools/explorer


#### Setup (to be deprecated)
To install the dependencies, please run `python setup.py install` from the following directories, in order:
* digitalbuildings/tools/validators/ontology_validator
* digitalbuildings/tools/validators/instance_validator
* digitalbuildings/tools/explorer

## Usage
There are two main ways in which the ontology explorer can be used:

1. Import explorer_handler from explorer.lib and call Build()
   * This returns an OntologyWrapper object which can be used to execute query functions on the Digital Buildings Ontology. You may also pass to Build() a path to an ontology extension.

2. As a stand-alone command-line interface (CLI). 
   * Run `python explorer.py` to start the application.
   * If you have extended the ontology by adding new types to your local ontology, run the following: `python explorer.py --modified-ontology-types=path/to/modified/ontology/types/folder`

