#!/usr/bin/env bash
set -e

TOOL="${1}"
if [ -z "${TOOL}" ]
then
  echo "Usage: digitalbuildings-tools <TOOL> [ARGS]" >&2
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
    exec python /source/tools/guid_generator/generator.py "${@}"
    ;;
  rdf_generator)
    exec python /source/tools/rdf_generator/rdfformat/rdf_generator.py "${@}"
    ;;
  scoring)
    exec python /source/tools/scoring/scorer.py "${@}"
    ;;
  instance_validator)
    exec python /source/tools/instance_validator/instance_validator.py "${@}"
    ;;
  ontology_validator)
    exec python /source/tools/ontology_validator/ontology_validator.py "${@}"
    ;;
  *)
    echo "ERROR: Unknown tool ${TOOL}" >&2
    ;;
esac
