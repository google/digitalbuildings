#!/bin/sh
shopt -s expand_aliases

echo "Starting setup..."

# handle different python alias
echo "Looking through possible python aliases"

REQUIRED_VERSION=3.9
POSSIBLE_ALIAS=("python3" "python" "py")
FOUND=false
for pa in "${POSSIBLE_ALIAS[@]}"
do
  which $pa
  EXIT_STATUS=$?
  if [ $EXIT_STATUS -ne 0 ]; then
    continue
  fi

  PYTHON_VERSION=$($pa -c 'import sys; version=sys.version_info[:2]; print("{}.{}".format(*version))')
  if [ $(printf "%s\n" "$PYTHON_VERSION" "$REQUIRED_VERSION" | sort -V -r | head -1) = "$PYTHON_VERSION" ] ; then
    if [ "$PYTHON_VERSION" = "$REQUIRED_VERSION" ] ; then
      echo "$PYTHON_VERSION is equal to $REQUIRED_VERSION"
    else
      echo "$PYTHON_VERSION is newer than $REQUIRED_VERSION"
    fi
    alias python=$pa
    FOUND=true
    break
  else
    echo "$PYTHON_VERSION is older than $REQUIRED_VERSION"
  fi
done

if ! $FOUND; then
  echo "Could not find a python 3.9 executable"
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
echo "Setup finished!"#!/bin/bash
