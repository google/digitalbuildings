@echo off
ECHO "Starting setup..."

:ontology_validator_setup
ECHO "Starting ontology validator setup"
CD validators\ontology_validator
START py setup.py install
ECHO "Finished ontology validator setup"
CD ..\..\

:instance_validator_setup
ECHO "Starting instance validator setup"
CD validators\instance_validator
START py setup.py install
ECHO "Finished instance validator setup"
CD ..\..

:explorer_setup
ECHO "Starting explorer setup"
CD explorer\
START py setup.py install
ECHO "Finished explorer setup"
CD ..

:guid_generator_setup
ECHO "Starting GUID generator setup"
CD guid_generator
START py setup.py install
ECHO "Finished GUID generator setup"
CD ..

:scoring_setup
ECHO "Starting scoring setup"
CD Scoring
START py setup.py install
ECHO "Finished Scoring setup"
CD ..

:rdf_generator_setup
ECHO "Starting RDF Generator setup"
CD rdf_generator
START py setup.py install
ECHO "Finihed Scoring setup"
CD ..

ECHO "Setup finished!"
PAUSE
