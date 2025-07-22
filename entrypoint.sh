#!/bin/bash
set -e

# wait for db and celery
sleep 10

python manage.py migrate --noinput

python manage.py load_customers

python manage.py load_loans

exec "$@"
