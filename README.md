[![Tools](https://github.com/google/digitalbuildings/actions/workflows/tools.yml/badge.svg)](https://github.com/google/digitalbuildings/actions/workflows/tools.yml)
![Ontology Type Validator](https://github.com/google/digitalbuildings/workflows/Ontology%20Type%20Validator/badge.svg)
![Node.js CI](https://github.com/google/digitalbuildings/workflows/Node.js%20CI/badge.svg)
[![GitHub stars](https://img.shields.io/github/stars/google/digitalbuildings.svg)](https://github.com/google/digitalbuildings/stargazers)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Digital Buildings Project

The Digital Buildings project is an open-source, Apache-licensed effort to create a uniform schema and toolset for representing structured information about buildings and building-installed equipment. A version of the Digital Buildings ontology and toolset is currently being used by Google to manage buildings in its portfolio. 

The Digital Buildings project originated from the need to manage a very large, heterogeneous building portfolio in a scalable way. The project aims to enable management applications/analyses that are trivially portable between buildings.  This goal is achieved through a combination of semantically-expressive abstract modeling, an easy-to-use configuration language, and robust validation tooling.  Digital Buildings work has been inspired by [Project Haystack](https://project-haystack.org/tag) and [BrickSchema](https://brickschema.org/) and maintains cross-compatibility and/or convergence as a long-term objective.

In creating the Digital Buildings project, we have considered the following:

* Human readability
* Machine readability and interpretation
* Composable functionality
* Dimensional analysis
* Correctness validation
* Cross-compatibility

## Project Structure

This project is structured as follows:
*  An [ontology](./ontology/README.md) that defines the parameters of the semantic data model ("Terminology box") and tools for building, validating, and associating real equipment with a specific model. It contains the following formats:
   * [Yaml format](./ontology/yaml/README.md)
   * [RDF/OWL format](./ontology/rdf/README.md)

* A [model instance configuration](./ontology/docs/building_config.md) (a.k.a building configuration file) that contains a mapping between the ontology and the "raw" data. Building configuration files are the "Assertion box."
* Tools that enable the following:
  * [**ABEL**](./tools/abel/README.md)**:** facilitates easier building configration construction by converting from a templatized Google Sheet to a [building configuration file](./ontology/docs/building_config.md) (and from a building configuration file back to a Google Sheet).
  * [**Explorer**](./tools/explorer/README.md)**:** allows users to explore ontology type fields and compare ontology types to each other.
  * [**Instance Validator**](./tools/validators/ontology_validator/README.md) which allows to validate the yaml ontology upon a change or an extension.
  * [**Ontology Validator**](./tools/validators/ontology_validator/README.md)**:** validates the ontology upon a change or an extension (currently only for the Yaml format).
  * [**RDF/OWL Generator**](./tools/rdf_generator/README.md)**:** generates an RDF version from the yaml ontology files.
* An [Internal Building Representation (IBR)](./ibr/README.md) file format to represent data from different verticals such as spatial or assets.

## Learning Modules
The learning modules provide an overview of the following key concepts:
* The main concepts and components of the Digital Buildings Ontology
* How to model entities and extend types in the ontology
* The components of building configuration files
* How to use the validation tools for ontology extensions and building configuration files

### Module 1: Digital Buildings Ontology (DBO)
In this module, you’ll fully explore the core modeling and organizational concepts of the DBO. These are essential concepts for data modeling and creating building configuration files.


* [Lesson 1: Introduction to the DBO](./ontology/docs/learning/Module_1_Lesson_1_Introduction_to_the_DBO.pdf)
* [Lesson 2: Conceptual model](./ontology/docs/learning/Module_1_Lesson_2_Conceptual_model.pdf)
* [Lesson 3: Subfields](./ontology/docs/learning/Module_1_Lesson_3_Subfields.pdf)
* [Lesson 4: Fields](./ontology/docs/learning/Module_1_Lesson_4_Fields.pdf)
* [Lesson 5: States and multi-states](./ontology/docs/learning/Module_1_Lesson_5_States_and_multistates.pdf)
* [Lesson 6: Entity types](./ontology/docs/learning/Module_1_Lesson_6_Entity_types.pdf)
* [Lesson 7: Mappings](./ontology/docs/learning/Module_1_Lesson_7_Mappings.pdf)
* [Lesson 8: Connections](./ontology/docs/learning/Module_1_Lesson_8_Connections.pdf)
* [Lesson 9: Namespaces](./ontology/docs/learning/Module_1_Lesson_9_Namespaces.pdf)


### Module 2: Data Modeling with the DBO

In this module, you’ll deepen your understanding of the DBO and practice applying it. Through several hands-on activities, you'll walk through the recommended workflow for creating a building configuration file


* [Lesson 1: Get ready to data model](./ontology/docs/learning/Module_2_Lesson_1_Get_ready_to_data_model.pdf)
* [Lesson 2: Determine which devices need to be modeled](./ontology/docs/learning/Module_2_Lesson_2_Determine_which_devices_need_to_be_modeled.pdf)
* [Lesson 3: Determine which data points are required](./ontology/docs/learning/Module_2_Lesson_3_Determine_which_data_points_are_required.pdf)
* [Lesson 4: Name each data point using the DBO](./ontology/docs/learning/Module_2_Lesson_4_Name_each_data_point_using_the_DBO.pdf)
* [Lesson 5: Propose an ontology extension](./ontology/docs/learning/Module_2_Lesson_5_Propose_an_ontology_extension.pdf)
* [Lesson 6: Construct and finalize the building configuration file](./ontology/docs/learning/Module_2_Lesson_6_Construct_and_finalize_the_building_configuration_file.pdf)
* [Lesson 7: Validate the instance and telemetry](./ontology/docs/learning/Module_2_Lesson_7_Validate_the_instance_and_telemetry.pdf)


## Issues
Please post issues in the [Issues](https://github.com/google/digitalbuildings/issues) section.

## Discussion
Our team has created an open mailing list to discuss Google's Digital Building effort. The discussion could include general questions, standards, APIs, and more. Join the discussion here: [google-digital-building-discuss@googlegroups.com](mailto:google-digital-building-discuss@googlegroups.com).

Members are expected to adhere to this code of conduct: [https://opensource.google.com/conduct](https://opensource.google.com/conduct).

## How to Contribute

Please see the [contribution](CONTRIBUTING.md) section.

## License
```
Copyright 2023 Google LLC

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

## Publications & Talks
* [Québec Bâtiment Vert et Intelligent 2020](https://www.eventbrite.ca/e/billets-rendez-vous-annuel-quebec-bvi-presente-par-google-128034116489)
* [ISWC 2020](http://ceur-ws.org/Vol-2721/paper510.pdf)
* [LDAC 2020](http://linkedbuildingdata.net/ldac2020/abstracts.html#industry10)
* [ICML 2020](http://proceedings.mlr.press/v119/sipple20a/sipple20a.pdf)
* [Semantics 2019](https://2019.semantics.cc/role-semantics-googles-smart-building-platform)
* [Google Cloud Next'19](https://youtu.be/Zz6jkLYkzSQ)
