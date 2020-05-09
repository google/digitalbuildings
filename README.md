![](https://github.com/google/digitalbuildings/workflows/python_tools/badge.svg)


# Digital Buildings Project

The Digital Buildings project is an open-source, Apache-licensed effort to create a uniform schema and toolset for representing structured information about buildings and building-inatalled equipment.  A version of the Digital Buildings ontology and toolset is currently being used by Google to manage buildings in its portfolio. 

The Digital Buildings project originated from the need to manage a very large, heterogeneous building portfolio in a scalable way. The project aims to enable management applications/analyses that are trivially portable between buildings.  This goal is achieved through a combination of semantically-expressive abstract modeling, an easy-to-use configuration language, and robust validation tooling.  Digital Buildings work has been inspired by [Project Haystack](https://project-haystack.org/tag) and [BrickSchema](https://brickschema.org/), and maintains cross-compatibility and/or convergence as a long-term objective.

In creating the Digital Buildings project, we have considered the following:

* Human Readability
* Machine readability and interpretation
* Composable functionality
* Dimesional Analysis
* Correctness validation
* Cross compatibility

## Project Structure

This project is structured as following:
*  An [**ontology**](/ontology/README.md) that defines the parameters of the semantic data model and tools for building, validating and associating real equipment with a specific model. It contains the following formats:
   * [Yaml format](/ontology/yaml/)
   * [RDF/OWL format](/ontology/rdf/)
* Tools which allow the following:
  * [Yaml Validator](/tools/validators/ontology_validator/README.md) which allows to validate the yaml ontology upon a change or an extension.
  * [RDF/OWL Generator](/tools/rdf_generator/README.md) which allows to generate an RDF version from the yaml ontology files.

## Discussion
Please post issues or discussion topics in [Issues](https://github.com/google/digitalbuildings/issues) section.


## How to Contribute

Please see the [contribution section](CONTRIBUTING.md)

## License
```
Copyright 2020 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

