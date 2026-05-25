 DevCollab API

A developer collaboration platform built with Django REST Framework.

## Features
- JWT Authentication
- Role-based permissions (Developer/Recruiter)
- Job listings with skill matching
- Application tracking system
- Posts and comments

## Tech Stack
- Python, Django, Django REST Framework
- JWT Authentication (SimpleJWT)
- SQLite (dev) / PostgreSQL (prod)

## Setup
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py runserver

## API Endpoints
...
