[![Django CI](https://github.com/KNaiskes/books-swapping/actions/workflows/django.yml/badge.svg)](https://github.com/KNaiskes/books-swapping/actions/workflows/django.yml)
# books-swapping
A simple platform to swap books with other users

### Preview
![1-ANIMATION](https://user-images.githubusercontent.com/6069054/144123865-ca3261a6-bb8c-4340-ad3e-eff24b75fa58.gif)

# Quick Start

### Clone this repository

```
$ git clone git@github.com:KNaiskes/books-swapping.git
```

### Create and activate a virtual enviroment

```
$ cd books-swapping/
$ python -m venv venv
$ source /venv/bin/activate
```

### Install dependencies

```
$ pip install -r requirements.txt
```

### Make migrations

```
$ python manage.py migrate
```

### Start development server

```
$ python manage.py runserver
```

# Use Docker and PostgreSQL (Optional)

### Requirements
- Docker
- Docker Compose

### Replace SQLite with PostgreSQL in settings.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

### Start Docker

```
$ sudo systemctl start docker
```

### Build the container

```
$ sudo docker-compose build
```

### Make migrations

```
$ sudo docker-compose run web python manage.py migrate
```

### Create admin user

```
$ sudo docker-compose run web python manage.py createsuperuser
```

### Start container

```
$ sudo docker-compose up
```
