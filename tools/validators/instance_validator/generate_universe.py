import sys
import os

def build_universe():
    """Generates ontology universe.

    Returns:
        Generated universe object.
    """
    # add universe building packages to path
    sys.path.append(os.path.abspath(os.path.join('..', 'ontology_validator'))) 
    # add ontology files to path
    sys.path.append(os.path.abspath(os.path.join('../../../', 'ontology')))

    from yamlformat.validator import external_file_lib
    from yamlformat.validator import namespace_validator
    from yamlformat.validator import presubmit_validate_types_lib

    yaml_files = external_file_lib._RecursiveDirWalk('../../../ontology/yaml/resources/')
    config = presubmit_validate_types_lib.SeparateConfigFiles(yaml_files)
    universe = presubmit_validate_types_lib.BuildUniverse(config)

    return universe

def parse_universe(universe):
    """Parses generated ontology universe object into its subcomponents

    Args:
        universe: generated ontology universe object

    Returns:
        fields: valid universe field types generated from ontology
        subfields_map: valid universe subfield types generated from ontology
        states_map: valid universe state types generated from ontology
        units_map:  valid universe unit types generated from ontology
        entities_map:  valid universe entity types generated from ontology
    """
    states = universe.state_universe
    entities = universe.entity_type_universe
    units = universe.unit_universe
    subfields = universe.subfield_universe

    # USAGE: fields.IsFieldDefined('process_return_water_temperature_sensor', '')
    fields = universe.field_universe

    # consolidate all entity information into dictionary
    entities_map = {}
    entity_type_namespaces = entities.type_namespaces_map
    for k in entity_type_namespaces.keys():
        valid_types_map = entity_type_namespaces[k].valid_types_map

        namespace = entity_type_namespaces[k].namespace
        entities_map[namespace] = {}

        for v_k in valid_types_map.keys():
            entity_type = valid_types_map[v_k]
            entities_map[namespace][v_k] = entity_type.GetAllFields(run_unsafe=True)
    
    subfields_map = subfields.GetSubfieldsMap('')
    states_map = states.GetStatesMap('')
    units_map = units.GetUnitsMap('')

    return fields, subfields_map, states_map, units_map, entities_map
