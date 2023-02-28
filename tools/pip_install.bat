@echo off
ECHO "Starting setup..."

:ontology_validator_setup
ECHO "Starting ontology validator setup"
CD validators\ontology_validator
START py -m pip install .
ECHO "Finished ontology validator setup"
CD ..\..\

:instance_validator_setup
ECHO "Starting instance validator setup"
CD validators\instance_validator
START py -m pip install .
ECHO "Finished instance validator setup"
CD ..\..

:instance_guid_generator_setup
ECHO "Starting instance GUID generator setup"
CD guid_generator\instance
START py -m pip install .
ECHO "Finished GUID generator setup"
CD ..\..

:ontology_guid_generator_setup
ECHO "Starting instance GUID generator setup"
CD guid_generator\ontology
START py -m pip install .
ECHO "Finished GUID generator setup"
CD ..\..

:abel_setup
ECHO "Starting ABEL setup"
CD abel
START py -m pip install .
ECHO "Finished ABEL setup"
CD ..

ECHO "Setup finished!"
PAUSE
