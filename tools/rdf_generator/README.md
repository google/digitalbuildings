# RDF Generator

The RDF Generator generates an OWL/RDF ontology from the yaml files.

It relies on the python library [RDFLib](https://github.com/RDFLib).

## Install

To install the generator and its dependencies:
1. Run `python3 -m pip install --upgrade pip` to ensure that your Python package management tools are up-to-date.
2. Run `python3 -m pip install -r requirements.txt ` from this directory.

## Run

The RDF Generator takes two arguments:
 
 * Input: the directory containing the yaml files.
 * Output: the file name/path where to generate the rdf ontology version.
 
 It can be executed as following:
 ```python rdfformat/rdf_generator.py --input=/PATH_TO_YAML_FILES --output=./digital_buildings.rdf```
