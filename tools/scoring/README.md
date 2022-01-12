# Scoring

The scoring tool evaluates _proposed_ configuration files against "known good" _solution_ files. It uses an F-score algorithm to provide floating-point representations of how closely the files compare along various _dimensions_.

## Install
To install the dependencies, please run the `python3 setup.py install` from the following directories, in order:
* digitalbuildings/tools/validators/ontology_validator
* digitalbuildings/tools/validators/instance_validator
* digitalbuildings/tools/scoring

## Usage

From the `scoring` directory: `python3 cli.py -ont path/to/ontology/yaml/resources -prop path/to/proposed/file.yaml -sol path/to/solution.file.yaml -v True`
