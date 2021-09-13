"""Sets up a minimal state universe required for testing."""

from yamlformat.validator import state_lib

STATE_FOLDER = state_lib.StateFolder(folderpath='states')
STATE_UNIVERSE = state_lib.StateUniverse(folders=[STATE_FOLDER])

STATE_FOLDER.AddFromConfig(
    config_filename='states/states.yaml',
    documents=[{
        'ON':
            'Powered on.',
        'OFF':
            'Powered off.',
        'AUTO':
            'Running under automatic control.',
        'MANUAL':
            'Running under manual (hand) control.',
        'OPEN':
            'Open position, typically for a valve or other pass-though.',
        'CLOSED':
            'Closed position, typically for a valve or other pass-though.',
        'LOW':
            'Low speed or output setting.',
        'MEDIUM':
            'Medium speed or output setting.',
        'HIGH':
            'High speed or output setting.',
        'OCCUPIED':
            'Occupied sensor state or operation mode.',
        'UNOCCUPIED':
            'Unoccupied sensor state or operation mode.',
        'COMMISSIONING':
            'The fan speed and valve positions are set to preconfigured parameters.',
        'FLUSHING':
            'The heating and cooling valves are fully open.',
        'HEATING':
            'The valve is in a heating configuration.',
        'COOLING':
            'The valve is in a cooling configuration.',
        'NEUTRAL':
            'Neither the heating valve nor cooling valve is open.',
        'ACCESS_FAILED':
            'The failure to access a resource.',
        'ACTIVE':
            'An action, activity, event, or operation is currently hapenning.',
        'CALENDAR_STARTUP':
            'The calendar events synchronization is starting up.',
        'CALENDAR_SUCCESS':
            'The calendar events synchronization was successful.',
        'DISABLED':
            'Something is disabled.',
        'DOES_NOT_MATCH':
            'Two or more things do not match.',
        'ENABLED':
            'Something is enabled.',
        'INACTIVE':
            'An action, activity, event, or operation is not currently hapenning.',
        'MATCHES':
            'Two or more things match.',
        'SUBSCRIPTION_FAILED':
            'The calendar events subscription has failed.',
        'UNKNOWN':
            'The state is unknown.',
        'WAITING_FOR_RESPONSE':
            'The calendar events synchronization process is awaiting response.',
        'PRESENT':
            'Something is currently materialized physically (e.g. flowrate_status is present).',
        'ABSENT':
            'Something is currently not materialized (e.g. flowrate_status is absent). ',
        'CHARGING':
            'The act of storing (e.g. energy stored in a battery).',
        'DISCHARGING':
            'Release of something built up or retained for later use.',
        'STANDBY':
            'Waiting in a prepared state.',
        'REMOTE':
            'The control is operated remotely.',
        'LOCAL':
            'The control is operating locally and independently with the remote system.'
    }])
