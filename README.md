# AWS resources Karst project

## Project setup

After clone the project you need execute database migrations:
```commandline
docker-compose run web /usr/local/bin/python django_project/manage.py migrate
```

Then, create a django-admin superuser:
```commandline
docker-compose run web /usr/local/bin/python django_project/manage.py createsuperuser --username user --email user@gmail.com
```
This command will prompt password, password again, and confirm it.

Last step is collect static files:
```commandline
docker-compose run web /usr/local/bin/python django_project/manage.py collectstatic --no-input
```

## Reference documentation:
* [Django Development with docker compose](https://realpython.com/django-development-with-docker-compose-and-machine/)
* [Django dockerized application](https://realpython.com/django-setup/)
* [Django production docker setup](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)
* [Mozilla Django learn](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Authentication)
