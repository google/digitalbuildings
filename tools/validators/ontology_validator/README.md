# Validator

The Ontology Validator allows you to extend the ontology and then validate it to make sure it is comform to guidelines.

## Yaml Validator
The validator source code can be found [here](yamlformat/validator/validate_types.py).

The Validator is python based, it takes the following arguments:

* original `-o` or `--original`: a path pointing to the original files of the
  ontology.
* modified-type-filepath (optional) `-m` or `--modified-type-filepath`:
  a path pointing to the modified files of the ontology.
* interactive `-i` or `--interactive`:enables interactive mode.

The validator can be run as following: `python3 validator.py
-o=Users/foo/ontology/` or `python3 validator.py --original=
--original=Users/foo/ontology/`
