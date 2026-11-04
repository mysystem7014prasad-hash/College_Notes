#!/usr/bin/env bash
set -o errexit

python -m pip install -r requirements.txt
python colleague_portal/manage.py collectstatic --no-input
