#!/usr/bin/env bash
set -e

cd "$(dirname "${0}")"

if [ -z "${1}" ]
then
  echo "Usage: ${0} <service-account-name>" >&2
  exit 1
fi

SERVICE_ACCOUNT_NAME="${1}"

gcloud_adc_access_token() {
  gcloud auth application-default print-access-token
}

create_token_request() {
  TOKEN_REQUEST_PATH="$(mktemp)"
  cat > "${TOKEN_REQUEST_PATH}" <<EOF
{"scope":["https://www.googleapis.com/auth/spreadsheets"],"lifetime":"3600s"}
EOF
  echo "${TOKEN_REQUEST_PATH}"
}

acquire_access_token() {
  TOKEN_REQUEST_PATH="$(create_token_request)"
  curl --fail -X POST \
    -H "Authorization: Bearer $(gcloud_adc_access_token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    -d "@${TOKEN_REQUEST_PATH}" \
    "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/${SERVICE_ACCOUNT_NAME}:generateAccessToken"
  rm "${TOKEN_REQUEST_PATH}"
}

acquire_access_token > spreadsheet_token.json
