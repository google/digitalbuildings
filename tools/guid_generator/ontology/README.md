# Entity Types GUID Generator

The GUID Generator generates GUIDs for entity types in the ontology that have
missing `guid` fields.

## Workflow

This tool is automatically run with the Ontology Type Validator action. It takes
a single argument: `-f/--files`, the absolute file paths of the entity type YAML
files for which to generate GUIDs.
