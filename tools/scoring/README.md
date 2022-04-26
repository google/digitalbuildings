# Scoring

The scoring tool evaluates _proposed_ configuration files against "known good" _solution_ files. It uses a rudimentary [F-score algorithm](https://en.wikipedia.org/wiki/F-score) to provide floating-point representations of how closely the files compare along various [_dimensions_](#dimensions). Broadly, its process is thus:

1. Filter out irrelevant entities (e.g. those in the solution which have a noncanonical type)
2. Create pairs of entities from the _proposed_ and _solution_ lists by matching [`cloud_device_id`](https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#config-format) (for reporting devices) or raw field names (for virtual devices)
3. From each entity pair, isolate the attributes relevant for the dimension being scored and reduce their values to sets (e.g. [connections](https://github.com/google/digitalbuildings/blob/master/ontology/docs/ontology_config.md#connections))
4. Count the `intersection` and `difference` between the respective _proposed_ and _solution_ sets
5. Input these figures to the aforementioned scoring algorithm to produce a singular numeric score

## Install
To install the dependencies, please run the `python3 setup.py install` from the following directories, in order:
* digitalbuildings/tools/validators/ontology_validator
* digitalbuildings/tools/validators/instance_validator
* digitalbuildings/tools/scoring

## Usage

The application can be run from the command line. It takes three arguments:
1. `-prop/--proposed` (required): Absolute path for your proposed configuration file (to be scored)
2. `-sol/--solution` (required): Absolute path for your solution configuration file
3. `-m/--modified-types-filepath` (optional): Absolute path for the directory which contains your ontology. Defaults to `ontology/yaml/resources`

Example (from the `digitalbuildings` directory): `python3 tools/scoring/scorer.py -prop path/to/proposed/file.yaml -sol path/to/solution/file.yaml`

## Interpreting Results

Scores range from `-1.00`, which indicates that all attempts were _incorrect_, to `1.00`, which indicates that all attempts were _correct_. Thus, `0.00` indicates an equal number of correct and incorrect attempts. In the future, the output schema is likely to be expanded to provide greater context for each score.

For a description of each dimension, please see [Dimensions](#dimensions). The [DBO documentation](https://github.com/google/digitalbuildings/blob/master/ontology/README.md) is extremely helpful for understanding the concepts employed (which this tool attempts to quantify).

### Caveats

There are presently some limitations to consider when interpreting scores:

- Canonical entities

  Generally speaking, any solution entity with a noncanonical type is not used as a basis for scoring. This is especially relevant in the context of `result_reporting`; that value is derived from only those entities which did not link to virtual devices.

- Missing types

  Given the limitation above, missing types can have a significant impact on scores. To provide some visibility into this, missing types are counted when the application is instantiated and a summary is output to the console.

- `None` scores

  It is possible to receive a score of `None` if the application does not identify any relevant solution entities for that entity category and dimension (either by design or as a consequence of the inputs).

- Precision

  The virtual-entity matching algorithm used by the "entity type identification" and "entity point identification" dimensions is not presently deterministic, which infrequently results in scores with small variances.

## Dimensions

### Entity Connection Identification

Quantifies whether [connections](https://github.com/google/digitalbuildings/blob/master/ontology/docs/ontology_config.md#connections) between [entities](https://github.com/google/digitalbuildings/blob/master/ontology/docs/ontology.md#overview) were correctly and completely defined in the proposed file. **This considers all entities.**

### Entity Identification

Quantifies whether the correct [entities](https://github.com/google/digitalbuildings/blob/master/ontology/docs/ontology.md#overview) were included in the proposed file. **This considers only canonically typed solution entities.**

### Entity Point Identification

Quantifies whether the proposed file included the correct [points](https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#defining-translations) in each entity. **This considers only canonically typed solution entities.**

### Entity Type Identification

Quantifies whether the proposed file assigned the correct [type](https://github.com/google/digitalbuildings/blob/master/ontology/docs/ontology_config.md#entitytypes) to each entity. **This considers only canonically typed solution entities.**

### Raw Field Selection

Quantifies whether the correct [raw fields](https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#defining-translations) were selected in the proposed file. **This considers only canonically typed reporting solution entities.**

### Standard Field Naming

Quantifies whether the correct [standard field names](https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#defining-translations) were selected in the proposed file. **This considers only canonically typed reporting solution entities.**

### State Mapping

Quantifies how accurately the proposed file mapped [multi-state values](https://github.com/google/digitalbuildings/blob/master/ontology/docs/ontology.md#multi-state-values) for relevant fields. **This considers only canonically typed reporting solution entities.**

### Unit Mapping

Quantifies how accurately the proposed file mapped [dimensional units](https://github.com/google/digitalbuildings/blob/master/ontology/docs/ontology.md#dimensional-units) for relevant fields. **This considers only canonically typed reporting solution entities.**
