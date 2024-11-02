#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput
cp -r /app/static_for_copy/. /app/static/

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
python manage.py createsuperuser --noinput


# Start server
echo "Starting server"
python -m gunicorn apps.core.asgi:application --worker-class uvicorn.workers.UvicornWorker --bind ${HOST}:${PORT}
