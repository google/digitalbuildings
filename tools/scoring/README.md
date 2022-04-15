# Scoring

The scoring tool evaluates _proposed_ configuration files against "known good" _solution_ files. It uses an F-score algorithm to provide floating-point representations of how closely the files compare along various _dimensions_.

## Install
To install the dependencies, please run the `python3 setup.py install` from the following directories, in order:
* digitalbuildings/tools/validators/ontology_validator
* digitalbuildings/tools/validators/instance_validator
* digitalbuildings/tools/scoring

## Usage

The application can be run from the command line. It takes three arguments:
1. `-ont/--ontology` (required): Absolute path for the directory which contains your ontology
2. `-prop/--proposed` (required): Absolute path for your proposed configuration file (to be scored)
3. `-sol/--solution` (required): Absolute path for your solution configuration file

Example: `scoring % python3 scorer.py -ont path/to/ontology/yaml/resources -prop path/to/proposed/file.yaml -sol path/to/solution/file.yaml`

## Interpreting Results

Scores range from `-1.0`, which indicates that all attempts were _incorrect_, to `1.0`, which indicates that all attempts were _correct_. Thus, `0.0` indicates an equal number of correct and incorrect attempts. In the future, the output schema is likely to be expanded to provide greater context for each score.

For a general description of each dimension, please refer to their respective docstrings. The [DBO documentation](https://github.com/google/digitalbuildings/blob/master/ontology/README.md) is extremely helpful for understanding the concepts employed (which this tool attempts to quantify).

### Caveats

There are presently some limitations to consider when interpreting scores:

- Canonical entities

  Generally speaking, any entity with a noncanonical type is not scored. This is especially relevant in the context of `result_reporting`; that value is derived from only those entities which did not link to virtual devices.

- Missing types

  Given the limitation above, missing types can have a significant impact on scores. To provide some visibility into this, missing types are counted when the application is instantiated and a summary is output to the console.

- `None` scores

  It is possible to receive a score of `None` if the application does not identify any relevant solution entities for that entity type and dimension (either by design or as a consequence of the inputs).

- Precision

  The virtual-entity matching algorithm used by the "entity type identification" and "entity point identification" dimensions is not presently deterministic, which infrequently results in scores with small variances.
