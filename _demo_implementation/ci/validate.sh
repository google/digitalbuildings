#!/usr/bin/env bash
#
# Recommendation #6: run the checks in CI, not on someone's laptop.
#
# Four gates, cheapest first, so a failure is reported in seconds rather than
# minutes:
#
#   1. unit tests                    -- the mapping logic itself
#   2. ontology pin                  -- has the vendored vocabulary moved?
#   3. offline mapping validation    -- every site export we maintain
#   4. DBO instance validator        -- the upstream authority, if installed
#
# Exit non-zero on the first failure. Usage: ci/validate.sh [site-dir ...]

set -euo pipefail

DEMO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO_ROOT="$(cd "${DEMO_ROOT}/.." && pwd)"
PYTHON="${PYTHON:-python3}"

cd "${DEMO_ROOT}"

SITES=("$@")
if [[ ${#SITES[@]} -eq 0 ]]; then
  SITES=("${DEMO_ROOT}/sample_site")
fi

echo "==> 1/4 unit tests"
"${PYTHON}" -m pytest tests/ -q

echo
echo "==> 2/4 ontology pin"
# Exits 1 when the vendored ontology content no longer matches ontology_pin.yaml.
"${PYTHON}" -m bms_dbo ontology-info

echo
echo "==> 3/4 offline mapping validation"
for site in "${SITES[@]}"; do
  echo "--- ${site}"
  "${PYTHON}" -m bms_dbo validate --site "${site}"
  "${PYTHON}" -m bms_dbo export --site "${site}" \
      --out "${DEMO_ROOT}/out/$(basename "${site}").yaml"
done

echo
echo "==> 4/4 DBO instance validator"
INSTANCE_VALIDATOR="${REPO_ROOT}/tools/validators/instance_validator/instance_validator.py"
if [[ ! -f "${INSTANCE_VALIDATOR}" ]]; then
  echo "SKIPPED: ${INSTANCE_VALIDATOR} not found."
  echo "         This gate is the upstream authority -- do not ship without it."
  exit 0
fi
if ! "${PYTHON}" -c "import validate.handler" >/dev/null 2>&1; then
  echo "SKIPPED: instance validator is not installed in this environment."
  echo "         Install it with: cd ${REPO_ROOT}/tools && ./pip_install.sh"
  echo "         This gate is the upstream authority -- do not ship without it."
  exit 0
fi
for site in "${SITES[@]}"; do
  echo "--- $(basename "${site}")"
  "${PYTHON}" "${INSTANCE_VALIDATOR}" \
      -i "${DEMO_ROOT}/out/$(basename "${site}").yaml"
done

echo
echo "All gates passed."
