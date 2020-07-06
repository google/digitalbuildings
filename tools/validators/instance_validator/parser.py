from strictyaml import Map, MapPattern, Str, Optional, Any, load, Enum, Regex, Seq, YAMLValidationError

# TODO check all valid states and ontological references in next validation steps
schema = MapPattern(Str(), 
    Map({
        'type': Str(), 
        'id': Str(), 
        Optional('connections'): MapPattern(Str(), Str())
                               | Seq(MapPattern(Str(), Str())),
        Optional('links'): MapPattern(Str(), 
            MapPattern(Str(), Str())),
        Optional('translation'): Any(),
        Optional('metadata'): Any()
    }))

translation_schema = Str() | Any()

# TODO add manual check for translation_data_schema to de-duplicate units/unit_values/states
# TODO add all units/unit_values/states to translation_data_schema
translation_data_schema = Str() | Map({
                                    'present_value': Str(),
                                    Optional('states'): MapPattern(Str(), Str()),
                                    Optional('units'): Map({
                                        'key': Str(),
                                        'values': MapPattern(Str(), Str())
                                    }),
                                    Optional('unit_values'): MapPattern(Str(), Str())
                                })

def load_yaml_with_schema(filepath, schema):
    """Loads an instance YAML file and parses it based on a strictyaml-formatted YAML schema.

    Args:
        filepath: filepath location of the YAML file
        schema: YAML schema in strictyaml format

    Returns:
        Returns the parsed YAML data in a stricyaml-provided 
        datastructure which is similar to a Python dictionary.
    """
    f = open(filepath).read()

    try:
        parsed = load(f, schema)
        return parsed
    except YAMLValidationError as error:
        raise error

def parse_yaml(filename: str):
    """Loads an instance YAML file and parses it with multiple strictyaml-formatted YAML schemas.

    Args:
        filename: filepath location of the YAML file

    Returns:
        Returns the parsed YAML data in a stricyaml-provided 
        datastructure which is similar to a Python dictionary.
    """
    yaml = load_yaml_with_schema(filename, schema)

    top_name = yaml.keys()[0]

    if 'translation' in yaml[top_name].keys():
        translation = yaml[top_name]['translation']
        translation.revalidate(translation_schema)

        # TODO can this be automatically verified based on ontology?
        # if translation is not UDMI compliant
        if translation.data != 'COMPLIANT':
            translation_keys = translation.keys()

            for k in translation_keys:
                translation[k].revalidate(translation_data_schema)

    return yaml