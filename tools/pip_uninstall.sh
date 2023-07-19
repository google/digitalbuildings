#!/usr/bin/env bash
set -e

cd "$(dirname "${0}")"
source "scripts/lib.sh"

find_setup_py_projects | while read -r PROJECT_PATH
do
  pushd "${PROJECT_PATH}" > /dev/null
  PACKAGE_NAME="$("${PYTHON}" setup.py --name)"
  "${PYTHON}" -m pip uninstall -y "${PACKAGE_NAME}"
  popd > /dev/null
done
