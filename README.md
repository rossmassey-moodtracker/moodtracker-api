# moodtracker-api

Django/Django REST Framework (DRF) API

Can create and view log entries for **mood** (on scale 1-10) and 
the **time** of entry

Requires authentication to view logs (for own user)

## Requirements
- Python v3.9
- _or_ Docker

#### Database Acess

`DB_PASSWORD` environment variable must be set to access the AWS RDS instance

- For ECS, this is done automatically as part of the GitHub action

- For local development, it can be set in an `.env` file in root of repository

## Local Environment Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run development server
```bash
./manage.py runserver
```

### Run tests
```bash
./manage.py test
```

## Docker

This API can be ran as a container

1. Build image and tag as `moodtracker-api`

    ```bash
    docker build -t moodtracker-api .
    ```

2. Run container and bind to port `8000`

    ```bash
    docker run -p 8000:8000 moodtracker-api
    ```

## Deployment

[![Deploy to Amazon ECS](https://github.com/rossmassey-moodtracker/moodtracker-api/actions/workflows/deploy-to-ecs.yaml/badge.svg)](https://github.com/rossmassey-moodtracker/moodtracker-api/actions/workflows/deploy-to-ecs.yaml)

This API is 
- built as a container image
- pushed to AWS ECR (Elastic Container Registry)
- deployed to ECS (Elastic Container Service)
- accessed through an ELB (Elastic Load Balancer)

through a GitHub action

It is published at:
http://moodtracker-api-load-balanacer-129190309.us-west-1.elb.amazonaws.com/

## Routes

### Django Admin

[/admin](http://moodtracker-api-load-balanacer-129190309.us-west-1.elb.amazonaws.com/admin/)

This is the Django admin site

### Swagger Docs

[/docs](http://moodtracker-api-load-balanacer-129190309.us-west-1.elb.amazonaws.com/docs/)

This shows all the API routes in an interactive browser

### Authentication

`/login` and `/signup` return a `<token>`

It can be added to request header as: 

`Authorization: Token <token>`

#### Signup

**POST** [/signup](http://moodtracker-api-load-balanacer-129190309.us-west-1.elb.amazonaws.com/signup/)
```
{
    "username": <username>, 
    "password": <password>, 
    "email": <email>
}
```

#### Login

**POST** [/login](http://moodtracker-api-load-balanacer-129190309.us-west-1.elb.amazonaws.com/login/)
```
{
    "username": <username>, 
    "password": <password>, 
}
```

### CRUD 

| Route | URL  | 
| --- | --- |
| [/api/moods](http://moodtracker-api-load-balanacer-129190309.us-west-1.elb.amazonaws.com/api/moods/) | logged moods for curent user |
