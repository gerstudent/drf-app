# Introduction

Repository contains sample API writen in Django REST framework. Project was created in educational
purposes.

- Available functions: view, send and delete posts (GET, POST, PUT, PATCH, DELETE), choice categories, authorization
  with sessions, simple tokens and JWT tokens.

# Prerequisites

Be sure you have the following installed on your development machine:

1. Python >= 3.7
2. Git
3. pip
4. Virtualenv

# Setup

To run this project in your development machine, follow these steps:

1. (optional) Create and activate a [virtualenv](https://virtualenv.pypa.io/)
   or [venv](https://docs.python.org/3/library/venv.html)

2. Ensure that the executable `pg_config` is available on your machine. You can check this using `which pg_config`. If
   not, install the dependency with one of the following.

- macOS: `brew install postgresql` using [Homebrew](https://brew.sh/)
- Ubuntu: `sudo apt-get install libpq-dev`
- [Others](https://stackoverflow.com/a/12037133/8122577)

3. Fork this repo and clone your fork:

   `git clone https://github.com/gerstudent/drf_app`

4. Install dependencies:

   `pip install -r requirements.txt`

5. Create a development database:

   `./manage.py migrate`

6. If everything is alright, you should be able to start the Django development server:

   `./manage.py runserver`

7. Open your browser and go to http://127.0.0.1:8000, you will be greeted with a welcome page.
