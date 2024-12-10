#!/bin/bash

source .venv/bin/activate
celery -A DNSAutocorrect beat -l info &
celery -A DNSAutocorrect worker -l info &
python manage.py runserver

