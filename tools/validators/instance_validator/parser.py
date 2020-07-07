import strictyaml

# TODO check all valid states and ontological references in next validation steps
_SCHEMA = strictyaml.MapPattern(strictyaml.Str(), 
    strictyaml.Map({
        'type': strictyaml.Str(), 
        'id': strictyaml.Str(), 
        strictyaml.Optional('connections'): strictyaml.MapPattern(strictyaml.Str(), strictyaml.Str())
                               | strictyaml.Seq(strictyaml.MapPattern(strictyaml.Str(), strictyaml.Str())),
        strictyaml.Optional('links'): strictyaml.MapPattern(strictyaml.Str(), 
            strictyaml.MapPattern(strictyaml.Str(), strictyaml.Str())),
        strictyaml.Optional('translation'): strictyaml.Any(),
        strictyaml.Optional('metadata'): strictyaml.Any()
    }))

_TRANSLATION_SCHEMA = strictyaml.Str() | strictyaml.Any()

# TODO add manual check for translation_data_schema to de-duplicate units/unit_values/states
# TODO add all units/unit_values/states to translation_data_schema
_TRANSLATION_DATA_SCHEMA = strictyaml.Str() | strictyaml.Map({
                                    'present_value': strictyaml.Str(),
                                    strictyaml.Optional('states'): strictyaml.MapPattern(strictyaml.Str(), strictyaml.Str()),
                                    strictyaml.Optional('units'): strictyaml.Map({
                                        'key': strictyaml.Str(),
                                        'values': strictyaml.MapPattern(strictyaml.Str(), strictyaml.Str())
                                    }),
                                    strictyaml.Optional('unit_values'): strictyaml.MapPattern(strictyaml.Str(), strictyaml.Str())
                                })

def _load_yaml_with_schema(filepath, schema):
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
        parsed = strictyaml.load(f, schema)
        return parsed
    except strictyaml.YAMLValidationError as error:
        raise error

def parse_yaml(filename: str):
    """Loads an instance YAML file and parses it with multiple strictyaml-formatted YAML schemas.

    Args:
        filename: filepath location of the YAML file

    Returns:
        Returns the parsed YAML data in a stricyaml-provided 
        datastructure which is similar to a Python dictionary.
    """
    yaml = _load_yaml_with_schema(filename, _SCHEMA)

    top_name = yaml.keys()[0]

    if 'translation' in yaml[top_name].keys():
        translation = yaml[top_name]['translation']
        translation.revalidate(_TRANSLATION_SCHEMA)

        # TODO can this be automatically verified based on ontology?
        # if translation is not UDMI compliant
        if translation.data != 'COMPLIANT':
            translation_keys = translation.keys()

            for k in translation_keys:
                translation[k].revalidate(_TRANSLATION_DATA_SCHEMA)

    return yaml