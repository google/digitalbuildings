# Ontology Explorer

The Ontology explorer allows a user to ask a few basic question of the ontology:
* What fields are associated with a type name
* What are the types associated with a given set of fields
* Is a field defined within a certain namespace

## Install

There are two ways to install the explorer.

## Pip

1. Run `python3 -m pip install --upgrade pip` to ensure that your Python package management tools are up-to-date.
2. Run `python3 -m pip install -r requirements.txt ` from the following directories, in order:
* digitalbuildings/tools/validators/ontology_validator
* digitalbuildings/tools/validators/instance_validator
* digitalbuildings/tools/explorer

### Setup
To install the dependencies, please run `python setup.py install` from the following directories, in order:
* digitalbuildings/tools/validators/ontology_validator
* digitalbuildings/tools/validators/instance_validator
* digitalbuildings/tools/explorer

## Usage
There are two main ways in which the ontology explorer can be used:
1. Import explorer_handler from explorer.lib and call Build()
  * This returns an OntologyWrapper object which can be used to execute query functions on the Digital Buildings Ontology. You may also pass to Build() a path to an ontology extension.
2. The explorer may also be run as a stand-alone command-line interface. 
  * Run `python explorer.py` to start the application.
  * If you have extended the ontology by adding new types to your local ontology, run the following: `python explorer.py --modified-ontology-types=path/to/modified/ontology/types/folder`

