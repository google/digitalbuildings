# Validator

The Ontology Validator allows you to extend the ontology and then validate it to make sure it is comform to guidelines.

## Yaml Validator
The validator source code can be found [here](https://github.com/google/digitalbuildings/tree/master/validators/ontology_validator/yamlformat).

The Validator is python based, it takes the following arguments:

* original: a path pointing to the original files of the ontology
* changed (optional): a path pointing to the changed files of the ontology.

The validator can be run as following: `python3 validator.py
--original=Users/foo/ontology/`
