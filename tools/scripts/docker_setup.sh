#!/usr/bin/env bash
set -e

python -m venv /env
source /env/bin/activate
cd /source/tools
mkdir ./.app_data
./pip_install.sh
pip install -r /source/requirements.txt
