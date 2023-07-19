#!/usr/bin/env bash
set -e

cd "$(dirname "${0}")"
source "scripts/lib.sh"

find_setup_py_projects | while read -r PROJECT_PATH
do
  pushd "${PROJECT_PATH}" > /dev/null
  "${PYTHON}" -m pip install .
  popd > /dev/null
done
