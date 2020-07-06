def validate_type(entity: dict, entities_map):
    entity_type_str = str(entity['type'])
    type_parse = entity_type_str.split('/')

    if len(type_parse) != 2:
        raise Exception('type improperly formatted:', entity_type_str)

    namespace = type_parse[0]
    entity_type = type_parse[1]

    if namespace not in entities_map.keys():
        raise Exception('invalid namespace:', namespace)
    
    if entity_type not in entities_map[namespace].keys():
        raise Exception('invalid entity type:', entity_type)

def validate_entity(entity: dict, fields, subfields_map, states_map, units_map, entities_map):
    validate_type(entity, entities_map)