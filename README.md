# Digital Buildings Ontology

The Digital Buildings ontology is an open-source, Apache-licensed development effort to create a uniform schema for representing metadata in Google's buildings real estate portfolio. It is inspired from [Project Haystack](https://project-haystack.org/tag) and [BrickSchema](https://brickschema.org/).

This repository tracks the main schema development of the Digital Buildings Ontology.


## Discussion
Discussion takes place primarily on the Digital Buildings User Form: [google-digital-building-discuss@googlegroups.com](mailto:google-digital-building-discuss@googlegroups.com)


## How to Contribute

Please see the [contribution section](./CONTRIBUTING.md)

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

## Ontology

The ontology description and organization is [here](./ontology/ontology.md).

The ontology is released in two formats:

* RDF: An RDF class hierarchy describing the various building subsystems and the entities and equipment therein A minimal, principled set of relationships for connecting these entities together into a directed graph representing a building A method of encapsulation for composing complex components from a set of lower-level ones. The rdf content can be found [here](/ontology/rdf)

* Yaml: An equivalent yaml representation of the RDF version for non-RDF experts. The yaml content can be found [here](/ontology/yaml)

