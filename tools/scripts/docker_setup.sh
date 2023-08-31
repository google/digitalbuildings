#!/usr/bin/env bash
set -e

python -m venv /env
source /env/bin/activate
cd /source/tools
./pip_install.sh
pip install -r /source/requirements.txt
mkdir /source/tools.app_data
mkdir /source/tools/.app_data/uploads
mkdir /source/tools/.app_data/reports
