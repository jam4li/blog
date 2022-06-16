# Blog

This project is written in Django. It contains the main principles of:
* Django Rest Framework
* Dockerizing
* Template Structure
* Test Driven Development

# Table of Contents
* [Installation](#installation)
* [Project Directory Structure](#project-directory-structure)

## Installation
We’ll assume you have installed <a href="https://docs.docker.com/engine/install/" target="_blank">Docker</a> and <a href="https://docs.docker.com/compose/install/" target="_blank">Docker-Compose</a> already.

You can check the version of Docker and Docker-Compose by running the following commands.
```bash
$ docker --version
Docker version 20.10.14, build a224086

$ docker-compose --version
docker-compose version 1.29.2, build 5becea4c
```
Now it's time to run the project by the following commands.
```bash
# Build images in the docker-compose.yaml file.
$ docker-compose build
 
# Build the images if they are not located locally and starts the containers.
$ docker-compose up -d
```
If we didn't get any errors by running two above commands, we can check the local server which is up right now.
| WARNING: The default port of a django local server is 8000, but because of using nginx we shouldn't enter the port! |
| --- |
Go to <a href="http://localhost/" target="_blank">localhost</a> in your browser, and you should see the default django page.

## Project Directory Structure
```bash
.
├── blog
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_views.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── data
│   └── nginx
│       └── app.conf
├── Dockerfile
├── docker-compose.yaml
├── entrypoint.sh
├── env
├── .env
├── locale
├── README.md
├── requirements.txt
├── media
├── static
│   ├── css
│   │   └── styles.css
│   ├── img
│   │   ├── favicon.ico
│   │   └── profile.jpg
│   └── js
│       └── scripts.js
└── templates
    ├── __base.html
    └── home
        └── index.html
```
