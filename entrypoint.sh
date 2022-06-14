#!/bin/bash

if [ "$DJANGO_DB_ENGINE" == "django.db.backends.postgresql_psycopg2" ]
then
    echo "Waiting for postgre..."

    while ! nc -z "$POSTGRES_DB" "$POSTGRES_PORT"; do
      sleep 0.1
    done

    echo "DB started"
fi

python manage.py makemigrations sales
python manage.py migrate
export DJANGO_SETTINGS_MODULE="config.settings"


python manage.py runserver 0.0.0.0:8000

exec "$@"
