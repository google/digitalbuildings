#!/bin/sh
shopt -s expand_aliases

echo "Starting setup..."

# handle different python alias
echo "Looking through possible python aliases"
alias PYTHON3="which python3"
alias PYTHON="which python"
alias PY="which py"

PYTHON3 > /dev/null
PYTHON3_EXIT_STATUS=$?
PYTHON > /dev/null
PYTHON_EXIT_STATUS=$?
PY > /dev/null
PY_EXIT_STATUS=$?

if [ "$PYTHON3_EXIT_STATUS" -eq 0 ]; then
  alias python='f(){ python3 "$@"; }; f'
elif [ "$PYTHON_EXIT_STATUS" -eq 0 ]; then
  alias python='f(){ python "$@"; }; f'
elif [ "$PY_EXIT_STATUS" -eq 0 ]; then
  alias python='f(){ py "$@"; }; f'
else
  echo "Could not find python executable"
  exit 125
fi

echo "Python executable found"

ontology_validator_setup()
{
  echo "Starting ontology validator setup"
  cd validators/ontology_validator
  python setup.py install
  echo "Finished ontology validator setup"
  cd ../..
}

instance_validator_setup()
{
  echo "Starting instance validator setup"
  cd validators/instance_validator
  python setup.py install
  echo "Finished instance validator setup"
  cd ../..
}

explorer_setup()
{
  echo "Starting explorer setup"
  cd explorer/
  python setup.py install
  echo "Finished explorer setup"
  cd ..
}

guid_generator_setup()
{
  echo "Starting GUID generator setup"
  cd guid_generator
  python setup.py install
  echo "Finished GUID generator setup"
  cd ..
}

scoring_setup()
{
  echo
  "Starting scoring setup"
  cd scoring
  python setup.py install
  echo "Finished Scoring setup"
  cd ..
}

rdf_generator_setup()
{
  echo "Starting RDF Generator setup"
  cd rdf_generator
  python setup.py install
  echo "Finihed Scoring setup"
  cd ..
}

ontology_validator_setup
instance_validator_setup
explorer_setup
guid_generator_setup
#scoring_setup
#rdf_generator_setup
echo "Setup finished!"
