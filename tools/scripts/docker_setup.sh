#!/usr/bin/env bash
set -e

python -m venv /env
source /env/bin/activate
cd /source/tools
mkdir ./.app_data
mkdir ./.app_data/uploads
mkdir ./.app_data/reports
./pip_install.sh
pip install -r /source/requirements.txt
