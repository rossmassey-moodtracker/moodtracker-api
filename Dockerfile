# Dockerfile to create an image that runs the moodtracker-api

FROM python:3.9-slim

# no .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# output to terminal immediately
ENV PYTHONUNBUFFERED 1

# work directory inside container
WORKDIR /app

# dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# copy files to container
COPY . /app/

# collect static files
RUN python manage.py collectstatic --noinput

# make entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# document port this image will listen on
EXPOSE 8000

# start the application
CMD ["/app/entrypoint.sh"]
