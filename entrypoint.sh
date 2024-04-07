#!/bin/bash
#
# API initialization and start script
#
# gunicorn HTTP server + nginx

# stop on error
set -e

# enable nginx config
rm -f /etc/nginx/sites-enabled/default
cp nginx.conf /etc/nginx/sites-available/nginx.conf
ln -sf /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled

# static files for django admin site
python3 manage.py collectstatic --noinput
chmod -R 755 /app/static

# database migrations
python3 manage.py migrate

# check nginx conf
nginx -t

# start api
service nginx start
exec gunicorn --workers 3 --bind unix:/app/gunicorn.sock api.wsgi:application
