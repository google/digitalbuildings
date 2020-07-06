import parser
import sys
# ONTOLOGY VALIDATION
# import ontology_validation
# import generate_universe

# TODO add input and return type checks in all functions

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('USAGE: python3 schema.py yaml_file_path')
        sys.exit(1)
    
    # SYNTAX VALIDATION
    print('\nValidator starting ...')
    filename = sys.argv[1]

    # throws errors for syntax
    parsed = dict(parser.parse_yaml(filename))

    print('Passed syntax checks!')

    # ONTOLOGY VALIDATION
    '''
    print('Building ontology universe ...')

    universe = generate_universe.build_universe()
    fields, subfields_map, states_map, units_map, entities_map = generate_universe.parse_universe(universe)

    entity_names = list(parsed.keys())

    for name in entity_names:
        entity = dict(parsed[name])
        ontology_validation.validate_entity(entity, fields, subfields_map, states_map, units_map, entities_map)

    print('Passed all checks!\n')
    '''