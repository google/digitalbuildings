![](https://github.com/google/digitalbuildings/workflows/Tools/badge.svg)
![Ontology Type Validator](https://github.com/google/digitalbuildings/workflows/Ontology%20Type%20Validator/badge.svg)
![Node.js CI](https://github.com/google/digitalbuildings/workflows/Node.js%20CI/badge.svg)
[![GitHub stars](https://img.shields.io/github/stars/google/digitalbuildings.svg)](https://github.com/google/digitalbuildings/stargazers)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Digital Buildings Project

The Digital Buildings project is an open-source, Apache-licensed effort to create a uniform schema and toolset for representing structured information about buildings and building-installed equipment. A version of the Digital Buildings ontology and toolset is currently being used by Google to manage buildings in its portfolio. 

The Digital Buildings project originated from the need to manage a very large, heterogeneous building portfolio in a scalable way. The project aims to enable management applications/analyses that are trivially portable between buildings.  This goal is achieved through a combination of semantically-expressive abstract modeling, an easy-to-use configuration language, and robust validation tooling.  Digital Buildings work has been inspired by [Project Haystack](https://project-haystack.org/tag) and [BrickSchema](https://brickschema.org/), and maintains cross-compatibility and/or convergence as a long-term objective.

In creating the Digital Buildings project, we have considered the following:

* Human Readability
* Machine readability and interpretation
* Composable functionality
* Dimensional Analysis
* Correctness validation
* Cross compatibility

## Project Structure

This project is structured as following:
*  An [**ontology**](/ontology/README.md) that defines the parameters of the semantic data model and tools for building, validating and associating real equipment with a specific model. It contains the following formats:
   * [Yaml format](/ontology/yaml/README.md)
   * [RDF/OWL format](/ontology/rdf/README.md)
* Tools which allow the following:
  * [Yaml Validator](/tools/validators/ontology_validator/README.md) which allows to validate the yaml ontology upon a change or an extension.
  * [RDF/OWL Generator](/tools/rdf_generator/README.md) which allows to generate an RDF version from the yaml ontology files.
* [Internal Building Representation](/ibr/README.md) (IBR) File Format to represent data from different verticals such as spatial, assets.

## Learning Modules

### Module 1
1. Introduction to the Digital Buildings Ontology [Lesson 1](https://docs.google.com/presentation/d/e/2PACX-1vRyKn-NaOsMSAOPsD9a7cYq3WQZ_ewRmwZfO_jd0imPwVOr9dMqR5DsHsRuq4SAoH5F0K9GKfyOF-5D/pub?start=false&loop=false&delayms=3000&slide=id.g1077f660f78_0_588)
2. Conceptual Model [Lesson 2](https://docs.google.com/presentation/d/e/2PACX-1vS3KhB7KBo2VBqfus4_zzSuDgtjOuXEdd56sHtr_7ZWa4PaIYBvXlt_oeG_9wX5pTappn71xIWiOQWN/pub?start=true&loop=false&delayms=3000)
3. Subfields [Lesson 3](https://docs.google.com/presentation/d/e/2PACX-1vQDljgWdSFbiJcVNdnUAkyeJkGzzkesXenMGLAMXA19-eR4V7Izp-xAiPy8j2Ex84UWO2aF1zp7Y9bT/pub?start=true&loop=false&delayms=3000)
4.  Fields [Lesson 4](https://docs.google.com/presentation/d/e/2PACX-1vSwmAWfAHHI2Hvu84PZyRYe0WXLjIpY4oCMSIbHxfw-evB-MQIz0mGZNPoZ201fWjsVtLThwg9PxyNJ/pub?start=true&loop=false&delayms=3000)
5.  States and Multi-states [Lesson 5](https://docs.google.com/presentation/d/e/2PACX-1vSIHnGIKoFlOKE3nejXGDmBgUAcNRuVOqQTwpN57kmw5H0OSBPDwrR64mNQ58XgweYI35X7dH3WZlPF/pub?start=true&loop=false&delayms=3000)
6.  Entity Types [Lesson 6](https://docs.google.com/presentation/d/e/2PACX-1vSuPHQ-BZ1biSQbt1Ilx8H1eS2cHPOF89oifLn1mdO5Me4y_ioHov_sghUYId35i5RMhMc0Ju_Ing1p/pub?start=true&loop=false&delayms=3000)
7.  Mappings [Lesson 7](https://docs.google.com/presentation/d/e/2PACX-1vQvTB0KgLgAEB0otrIfd3AcHsUtHUqEDls5rCaHaj7Dr8J6YDVuF9-flN6E0dy72jJBVxMM58CsHOrY/pub?start=true&loop=false&delayms=3000)
8.  Connections [Lesson 8](https://docs.google.com/presentation/d/e/2PACX-1vTXIp33hO6bmRAfusPE0Gwtpcs_ZWkYt4y295PVdQB2l4DOibn4tx-2XK56mk_be7Ycxm92WOQBEeXO/pub?start=true&loop=false&delayms=3000)
9.  Namespaces [Lesson 9](https://docs.google.com/presentation/d/e/2PACX-1vRNwLAMtnkzVeJL-qOriEO7rotpdi6YYM9HRcX6oeB0sUqx4Y6aKthzOvuTm4cqYUJOKFebdbIRU_Ew/pub?start=true&loop=false&delayms=3000)

### Module 2
1. Get ready to Data Model [Lesson 1](https://docs.google.com/presentation/d/e/2PACX-1vSKWuC6f9aWSPRVmpVEpiO3AujUY2jvJ9_3a9K7z5DbuwhqmU_9_P11UhwVoee4EPQNcpRjw6aSMzZE/pub?start=true&loop=false&delayms=3000)
2. Determin which devices need to be modeled [Lesson 2](https://docs.google.com/presentation/d/e/2PACX-1vTjKitx4COQYLK5UZbc_FL1_TRk7ui4cKq6V3FIRJq41KDzAumvJckslQJb6bZRvOZfkryiNFNCSMg1/pub?start=true&loop=false&delayms=3000)
3. Determin which data points are required [Lesson 3](https://docs.google.com/presentation/d/e/2PACX-1vTJCY8C35ANXSxomB1JNSqQ4QqBdgoFWeitPVSjbk0jnpXpKordiWLPN2VuO82-2p7ndzFXmtgQVKjb/pub?start=true&loop=false&delayms=3000)
4. Get ready to Data Model [Lesson 4](https://docs.google.com/presentation/d/e/2PACX-1vR3ekSD5dW_78WXkaWKDfaaQr1526n0p-_wn-v4NqCuaDXtxFDjuEra_aJyPpJ3cn7Jcd-LI8lq3NFL/pub?start=true&loop=false&delayms=3000)
5. Get ready to Data Model [Lesson 5](https://docs.google.com/presentation/d/e/2PACX-1vRQgMCP9-s6kwQ4_TOeW9iFNA4DzEXGcbES9rLKuUxoKhwy3l3p1nC6a2_NjpOXuTllumy79VZwTzRA/pub?start=true&loop=false&delayms=3000)
6. Get ready to Data Model [Lesson 6](https://docs.google.com/presentation/d/e/2PACX-1vQXGvKZ4LOoDpZ_Ru7CJ-9AsQk0Bfj2X4pspyasIek3rIg0jeArWeGdyPUOS-MxJgwP1wpyPDH8RYjG/pub?start=true&loop=false&delayms=3000)
7. Get ready to Data Model [Lesson 7](https://docs.google.com/presentation/d/e/2PACX-1vTsqYULOuBsC_-CE6SsFVi7nTXgOI9T75CKUCLV1fGASU--m1TDtEYeEju2rjpgHr0wQfofR_QNyRrI/pub?start=true&loop=false&delayms=3000)

## Issues
Please post issues in [Issues](https://github.com/google/digitalbuildings/issues) section.

## Discussion
Open mailing list to discuss Google's Digital Building effort. Discussion could include general questions, standards, APIs, and more. [google-digital-building-discuss@googlegroups.com](mailto:google-digital-building-discuss@googlegroups.com)

Members are expected to adhere to this code of conduct: [https://opensource.google.com/conduct](https://opensource.google.com/conduct)

## How to Contribute

Please see the [contribution section](CONTRIBUTING.md)

## License
```
Copyright 2022 Google LLC

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


