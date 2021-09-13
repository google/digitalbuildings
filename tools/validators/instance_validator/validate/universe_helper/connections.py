"""Sets up a minimal connection universe required for testing."""

from yamlformat.validator import connection_lib

CONNECTION_FOLDER = connection_lib.ConnectionFolder(folderpath='connections')
CONNECTION_UNIVERSE = connection_lib.ConnectionUniverse(
    folders=[CONNECTION_FOLDER])

CONNECTION_FOLDER.AddFromConfig(
    documents=[{
        'CONTAINS': {
            'description':
                'Source physically encapsulates at least part of Target.'
        },
        'CONTROLS': {
            'description':
                'Source determines or affects the internal state or behavior of Target.'
        },
        'FEEDS': {
            'description':
                'Source provides some media (ex: water or air) to Target.'
        },
        'HAS_PART': {
            'description':
                'Source has some component or part defined by Target.'
        },
        'HAS_RANGE': {
            'description':
                'Source has a coverage or detection range defined by Target.'
        },
    }],
    config_filename='connections/connections.yaml')
