#!/bin/sh

# database migrations
python manage.py migrate

# gunicorn WSGI HTTP server
exec gunicorn --bind 0.0.0.0:8000 api.wsgi:application
