#!/bin/sh

# Serve application
python3 -m gunicorn --bind 0.0.0.0:$APP_PORT app:app --workers 4
