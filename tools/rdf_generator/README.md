# RDF Generator

The RDF Generator generates an OWL/RDF ontology from the yaml files.

It relies on the python library [RDFLib](https://github.com/RDFLib).

## Run

The RDF Generator takes two arguments:
 
 * Input: the directory containing the yaml files.
 * Output: the file name/path where to generate the rdf ontology version.
 
 It can be executed as following:
 ```python rdfformat/rdf_generator.py --input=/PATH_TO_YAML_FILES --output=./digital_buildings.rdf```
