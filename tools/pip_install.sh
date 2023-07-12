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
  python -m pip install .
  echo "Finished ontology validator setup"
  cd ../..
}

instance_validator_setup()
{
  echo "Starting instance validator setup"
  cd validators/instance_validator
  python -m pip install .
  echo "Finished instance validator setup"
  cd ../..
}

explorer_setup()
{
  echo "Starting explorer setup"
  cd explorer
  python -m pip install .
  echo "Finished explorer setup"
  cd ..
}

instance_guid_generator_setup()
{
  echo "Starting Instance GUID generator setup"
  cd guid_generator/instance
  python -m pip install .
  echo "Finished instance GUID generator setup"
  cd ../..
}

ontology_guid_generator_setup()
{
  echo "Starting Ontology GUID generator setup"
  cd guid_generator/ontology
  python -m pip install .
  echo "Finished Ontology GUID generator setup"
  cd ../..
}

abel_setup()
{
  echo "Starting ABEL setup"
  cd abel
  python -m pip install .
  echo "Finished ABEL setup"
  cd ..
}


ontology_validator_setup
instance_validator_setup
explorer_setup
instance_guid_generator_setup
ontology_guid_generator_setup
abel_setup
echo "Setup finished!"
