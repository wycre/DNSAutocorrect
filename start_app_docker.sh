#!/bin/bash

/usr/bin/redis-server &
celery -A DNSAutocorrect beat -l info &
celery -A DNSAutocorrect worker -l info &
python manage.py runserver 0.0.0.0:8000

