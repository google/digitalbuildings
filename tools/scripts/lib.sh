#!/usr/bin/env bash
REQUIRED_PYTHON_VERSION="3.9"
DEFAULT_PYTHON_CHECK_NAMES=("python3" "python${REQUIRED_PYTHON_VERSION}" "python" "py")

if [ -n "${PYTHON}" ]
then
  PYTHON_CHECK_NAMES=("${PYTHON}")
else
  PYTHON_CHECK_NAMES=()
fi

# shellcheck disable=SC2206
PYTHON_CHECK_NAMES+=(${DEFAULT_PYTHON_CHECK_NAMES[@]})

get_python_version() {
  "${1}" -c 'import sys; version=sys.version_info[:2]; print("{}.{}".format(*version))'
}

version_greater_than_equal_to() {
  [ "$(printf "%s\n" "${1}" "${2}" | sort -V -r | head -1)" = "${1}" ]
}

find_compatible_python_version() {
  REQUIRED="${1}"
  INCOMPATIBLE_VERSIONS=()
  for PYTHON_EXE in "${PYTHON_CHECK_NAMES[@]}"
  do
    if ! "${PYTHON_EXE}" --version > /dev/null 2>&1
    then
      continue
    fi
    PYTHON_VERSION="$(get_python_version "${PYTHON_EXE}")"
    if version_greater_than_equal_to "${PYTHON_VERSION}" "${REQUIRED}"
    then
      echo "${PYTHON_EXE}"
      return
    else
      INCOMPATIBLE_VERSIONS+=("${PYTHON_EXE} = ${PYTHON_VERSION}")
    fi
  done

  if [ "${#INCOMPATIBLE_VERSIONS[@]}" = 0 ]
  then
    echo "ERROR: No compatible Python version found. Please install at least Python ${REQUIRED}" >&2
    exit 1
  fi
  echo "ERROR: Compatible Python version not found, expected at least Python ${REQUIRED} but found:" >&2
  for INCOMPATIBLE_VERSION in "${INCOMPATIBLE_VERSIONS[@]}"
  do
    echo "  ${INCOMPATIBLE_VERSION}" >&2
  done
  exit 1
}

find_setup_py_projects() {
  find . -type f -name 'setup.py' -mindepth 2 -maxdepth 3 | while read -r SETUP_PY_FILE
  do
    dirname "${SETUP_PY_FILE}"
  done
}

PYTHON="$(find_compatible_python_version "${REQUIRED_PYTHON_VERSION}")"
