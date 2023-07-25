#!/usr/bin/env bash
set -e

source /env/bin/activate

TOOL="${1}"
if [ -z "${TOOL}" ]
then
  echo "Usage: digitalbuildings <TOOL> [ARGS]" >&2
  exit 1
fi

shift

case "${TOOL}" in
  abel)
    exec python /source/tools/abel/abel.py "${@}"
    ;;
  explorer)
    exec python /source/tools/explorer/explorer.py "${@}"
    ;;
  guid_generator)
    exec python /source/tools/guid_generator/instance/instance_guid_generator.py "${@}"
    ;;
  rdf_generator)
    exec python /source/tools/rdf_generator/rdfformat/rdf_generator.py "${@}"
    ;;
  scoring)
    exec python /source/tools/scoring/scorer.py "${@}"
    ;;
  instance_validator)
    exec python /source/tools/validators/instance_validator/instance_validator.py "${@}"
    ;;
  ontology_validator)
    exec python /source/tools/validators/ontology_validator/yamlformat/validator.py "${@}"
    ;;
  console)
    exec python "${@}"
    ;;
  shell)
    exec bash "${@}"
    ;;
  *)
    echo "ERROR: Unknown tool ${TOOL}" >&2
    ;;
esac
