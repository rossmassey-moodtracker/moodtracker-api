# moodtracker-api

Django/Django REST Framework (DRF) API

Can create and view log entries for **mood** (on scale 1-10) and 
the **time** of entry

Requires authentication to view logs (for own user)

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


## API

### Swagger Docs

[/docs](http://127.0.0.1:8000/docs/)

This shows all the API routes in an interactive browser

### Authentication

`/login` and `/signup` return a `<token>`

It can be added to request header as: 

`Authorization: Token <token>`

#### Signup

**POST** [/signup](http://127.0.0.1:8000/signup/)
```
{
    "username": <username>, 
    "password": <password>, 
    "email": <email>
}
```

#### Login

**POST** [/login](http://127.0.0.1:8000/login/)
```
{
    "username": <username>, 
    "password": <password>, 
}
```

### CRUD Routes

| Route | URL  | 
| --- | --- |
| [/moods](http://127.0.0.1:8000/moods/) | logged moods for curent user |
