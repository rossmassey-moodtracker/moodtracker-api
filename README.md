# moodtracker-api

Django/Django REST Framework (DRF) API

Can create and view log entries for **mood** (on scale 1-10) and 
the **time** of entry

Requires authentication to view logs (for own user)

## Environment Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run development server
```bash
./manage.py runserver
```

## Routes

### Swagger
http://127.0.0.1:8000/docs/

### Authentication

`/login` and `/signup` return a `<token>`

It can be added to request header as: 

`Authorization: Token <token>`

#### Signup

http://127.0.0.1:8000/signup/ **(POST)**
```
{
    "username": <username>, 
    "password": <password>, 
    "email": <email>
}
```

#### Login

http://127.0.0.1:8000/signup/ (**POST**)
```
{
    "username": <username>, 
    "password": <password>, 
}
```

### MoodLog ###
http://127.0.0.1:8000/moods/

## Run tests
```bash
./manage.py test
```