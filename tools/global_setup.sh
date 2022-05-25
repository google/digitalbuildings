#!/bin/sh
echo "Starting setup..."

ontology_validator_setup()
{
  echo "Starting ontology validator setup"
  cd validators/ontology_validator
  python3 setup.py install
  echo "Finished ontology validator setup"
  cd ../..
}

instance_validator_setup()
{
  echo "Starting instance validator setup"
  cd validators/instance_validator
  python3 setup.py install
  echo "Finished instance validator setup"
  cd ../..
}

explorer_setup()
{
  echo "Starting explorer setup"
  cd explorer/
  python3 setup.py install
  echo "Finished explorer setup"
  cd ..
}

guid_generator_setup()
{
  echo "Starting GUID generator setup"
  cd guid_generator
  python3 setup.py install
  echo "Finished GUID generator setup"
  cd ..
}

scoring_setup()
{
  echo
  "Starting scoring setup"
  cd scoring
  python3 setup.py install
  echo "Finished Scoring setup"
  cd ..
}

rdf_generator_setup()
{
  echo "Starting RDF Generator setup"
  cd rdf_generator
  python3 setup.py install
  echo "Finihed Scoring setup"
  cd ..
}

ontology_validator_setup
instance_validator_setup
#explorer_setup
guid_generator_setup
#scoring_setup
#rdf_generator_setup
echo "Setup finished!"
