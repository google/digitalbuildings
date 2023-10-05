# Digitalbuildings Ontology

This section of the digitalbuildings tree contains configuration files and documentation for the digitalbuildings model.

The model is provided in the following file formats:
*    A [yaml](/ontology/yaml/README.md) version, which is the primary configuration source
*    A [RDF](/ontology/rdf/README.md) version that is generated from the yaml version using the [RDF Generator](/tools/rdf_generator/README.md)

Documentation for the model can be found in the [docs](docs/) folder.
*   [**Ontology Overview**](/ontology/docs/ontology.md)**:** provides an overview of the structure and first principles of the ontology
*   [**Ontology Configuration**](/ontology/docs/ontology_config.md)**:** explains how to write and validate the .yaml configuration files
*   [**Model**](/ontology/docs/model.md)**:** describes the conventions used in the provided abstract model
    * [**Model HVAC**](/ontology/docs/model_hvac.md)**:** specifically describes the application of the model in the HVAC namespace
        * [**AHU**](/ontology/docs/hvac_ahu.md)**:** example of the model applied to an air handling unit (AHU)
        * [**CHWS**](/ontology/docs/hvac_chws.md)**:** example of the model applied to a chilled water system (CHWS)
        * [**FCU**](/ontology/docs/hvac_fcu.md)**:** example of the model applied to a fan coil unit (FCU)
        * [**HWS**](/ontology/docs/hvac_hws.md)**:** example of the model applied to a heating water system (HWS)
*   [**Building Configuration**](/ontology/docs/building_config.md)**:** describes the configuration format for mapping concrete assets to a model and validating the mapping
* [**Frequenty Asked Questions**](/ontology/docs/faq.md)**:** centralized answers to frequently asked questions regarding the ontology

## Learning Modules
The learning modules provide an overview of the following key concepts:
* The main concepts and components of the Digital Buildings Ontology
* How to model entities and extend types in the ontology
* The components of building configuration files
* How to use the validation tools for ontology extensions and building configuration files

### Module 1: Digital Buildings Ontology (DBO)
In this module, you’ll fully explore the core modeling and organizational concepts of the DBO. These are essential concepts for data modeling and creating building configuration files.


* [Lesson 1: Introduction to the DBO](./docs/learning/Module_1_Lesson_1_Introduction_to_the_DBO.pdf)
* [Lesson 2: Conceptual model](./docs/learning/Module_1_Lesson_2_Conceptual_model.pdf)
* [Lesson 3: Subfields](./docs/learning/Module_1_Lesson_3_Subfields.pdf)
* [Lesson 4: Fields](./docs/learning/Module_1_Lesson_4_Fields.pdf)
* [Lesson 5: States and multi-states](./docs/learning/Module_1_Lesson_5_States_and_multistates.pdf)
* [Lesson 6: Entity types](./docs/learning/Module_1_Lesson_6_Entity_types.pdf)
* [Lesson 7: Mappings](./docs/learning/Module_1_Lesson_7_Mappings.pdf)
* [Lesson 8: Connections](./docs/learning/Module_1_Lesson_8_Connections.pdf)
* [Lesson 9: Namespaces](./docs/learning/Module_1_Lesson_9_Namespaces.pdf)


### Module 2: Module 2: Data Modeling with the DBO

In this module, you’ll deepen your understanding of the DBO and practice applying it. Through several hands-on activities, you'll walk through the recommended workflow for creating a building configuration file


* [Lesson 1: Get ready to data model](./docs/learning/Module_2_Lesson_1_Get_ready_to_data_model.pdf)
* [Lesson 2: Determine which devices need to be modeled](./docs/learning/Module_2_Lesson_2_Determine_which_devices_need_to_be_modeled.pdf)
* [Lesson 3: Determine which data points are required](./docs/learning/Module_2_Lesson_3_Determine_which_data_points_are_required.pdf)
* [Lesson 4: Name each data point using the DBO](./docs/learning/Module_2_Lesson_4_Name_each_data_point_using_the_DBO.pdf)
* [Lesson 5: Propose an ontology extension](./docs/learning/Module_2_Lesson_5_Propose_an_ontology_extension.pdf)
* [Lesson 6: Construct and finalize the building configuration file](./docs/learning/Module_2_Lesson_6_Construct_and_finalize_the_building_configuration_file.pdf)
* [Lesson 7: Validate the instance and telemetry](./docs/learning/Module_2_Lesson_7_Validate_the_instance_and_telemetry.pdf)

Enjoy!
