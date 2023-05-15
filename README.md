# Foodgram - Grocery assistant

[![Grocery assistant workflow](https://github.com/sushidze/recipes-assistant-react/actions/workflows/main.yml/badge.svg)](https://github.com/sushidze/recipes-assistant-react/actions/workflows/main.yml) 

## Technology stack

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

## Description of the project

Foodgram is a resource for publishing recipes.
Users can create their own recipes, read other users' recipes, subscribe to interesting authors, add the best recipes to favorites, and create a shopping list and download it in pdf format

## Installing the project locally

* Clone repository to local machine:
```bash
git clone https://github.com/sushidze/foodgram-project-react.git
cd foodgram-project-react
```

* Create and activate virtual environment:

```bash
python -m venv env
```

```bash
source env/bin/activate
```

* Create a `.env` file in the `/infra/` directory with the content:

```
SECRET_KEY=secret key django
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

* Go to directory and install dependencies from requirements.txt file:

```bash
cd backend/
pip install -r requirements.txt
```

* Run the migrations:

```bash
python manage.py migrate
```

* Start the server:
```bash
python manage.py runserver
```

## Running a project in a Docker container
* Install Docker.

The launch options are described in the `docker-compose.yml` and `default.conf` files located in the `infra/` directory.
If necessary, add/change project addresses in the `nginx.conf` file

* Run docker compose:
```bash
docker-compose up -d --build
```  
  > After assembly, 3 containers appear:
   > 1. database container **db**
   > 2. application container **backend**
   > 3. **nginx** web server container
* Apply migrations:
```bash
docker-compose exec backend python manage.py migrate
```
* Download ingredients:
```bash
docker-compose exec backend python manage.py fill_db
```
* Create an administrator:
```bash
docker-compose exec backend python manage.py createsuperuser
```
* Collect static:
```bash
docker-compose exec backend python manage.py collectstatic --noinput
```

## Website
The site is available at the following link:
[http://158.160.51.237/](http://158.160.51.237/)

## API Documentation
API documentation is available here (created with redoc):
[http://158.160.51.237/api/docs/](http://158.160.51.237/api/docs/)
