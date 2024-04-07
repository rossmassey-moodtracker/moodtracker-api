# Dockerfile to create an image that runs the moodtracker-api
#
# Installs python and nginx, plus other dependencies

FROM ubuntu:latest

ENV PYTHONUNBUFFERED=1

# container dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    nginx \
    vim

# work directory inside container
WORKDIR /app

# copy files
COPY . /app/

# python dependencies
RUN pip3 install -r requirements.txt

# entrypoint script
RUN chmod +x /app/entrypoint.sh

# document port container will listen on
EXPOSE 8000

# initializes and runs server
CMD ["/app/entrypoint.sh"]
