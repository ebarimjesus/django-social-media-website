#!/bin/bash

# Navigate to your Django project directory


python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic --noinput

python manage.py oscar_populate_countries

# Run Django development server
gunicorn social_book.wsgi:application --bind 0.0.0.0:8000

