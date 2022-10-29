#!/bin/bash
#sudo kill $(pgrep -f "/var/www/ml/venv/bin/python3 /var/www/ml/venv/bin/gunicorn")
source ./venv/bin/activate
python3 -m bot
