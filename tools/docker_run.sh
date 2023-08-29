#!/usr/bin/env bash
set -e

IMAGE_NAME="ghcr.io/google/digitalbuildings/tools"
IMAGE_TAG="latest"

PATH_TO_MOUNT="$(realpath .)"

cd "$(dirname "${0}")"
# shellcheck disable=SC2034
SKIP_PYTHON_CHECK=1
source "scripts/lib.sh"
pushd .. > /dev/null
docker build -q -t "${IMAGE_NAME}:${IMAGE_TAG}" . > /dev/null

MAYBE_GCLOUD_CREDENTIALS_PATH="${HOME}/.config/gcloud/application_default_credentials.json"
MAYBE_GCLOUD_CREDENTIALS_FLAGS=()

if [ -f "${MAYBE_GCLOUD_CREDENTIALS_PATH}" ]
then
  MAYBE_GCLOUD_CREDENTIALS_FLAGS+=(
    "-v"
    "${MAYBE_GCLOUD_CREDENTIALS_PATH}:/root/.config/gcloud/application_default_credentials.json"
  )
fi

# shellcheck disable=SC2068
exec docker run -p 5000:5000 -it -v "${PATH_TO_MOUNT}:/work" ${MAYBE_GCLOUD_CREDENTIALS_FLAGS[@]} "${IMAGE_NAME}:${IMAGE_TAG}" "${@}"
