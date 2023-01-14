#!/usr/bin/env bash
set -e

pip install virtualenv
virtualenv /env
source /env/bin/activate
cd /source/tools
./pip_install.sh
