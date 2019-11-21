# Heroku Django Vue Starter Template

A project starter template for Django 2.0 and VueJS
This template is based on https://github.com/heroku/heroku-django-template, which included:
- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.6 runtime environment.

It extends the template by adding:
 - Vue for increased front-end capabilities
 - Postgres for data storage
 - Celery for asyncronous task handling (including celery beat for regular tasks)
 - SendGrid for email
 - eslint, flake8, sylelint for linting
 - pre-commit so that the linters run on commit
 
Note: In this readme I provide somewhat "opinionated" instructions (for example using github).
This template should work with minimal changes deployed to other locations, or even not on Heroku (I use something similar for GKE), but I have not tested them.

Prerequisites:
 - Git (https://git-scm.com/downloads) and a GitHub account (https://github.com/)
 - Heroku account (www.heroku.com) and the Heroku CLI installed (https://devcenter.heroku.com/articles/heroku-cli)
 - Optional but recommended: Anaconda (python) installed (https://www.anaconda.com/distribution/). If not Anaconda, Python 3.6 of some kind installed
 - Node.js (https://nodejs.org/en/)
 - A local postgres installation, including psql (https://www.postgresql.org/download/)
## How to Use
In the instructions below, replace anything in square brackets `[]` with whatever you choose

To use this project, follow these steps:

- Create your working environment. I recommend conda: `conda create -n [PROJECT_NAME]env python=3.6`
- Activate that environment: `activate [PROJECT_NAME]env`
- Install Django (`$ pip install django`)
- Create a new project and install the Python and JS requirements
- Push the code to GitHub
- Set up the Heroku App
- Set up the local postgres database


### Creating your project and installing the requirements

- Create the template in the local directory
```
django-admin.py startproject --template=https://github.com/Bobstin/healthdiary/archive/master.zip --name=Procfile [PROJECT_NAME]
```
(If this doesn't work on windows, replace `django-admin.py` with `django-admin`)
- Install the requirements:
```
pip install -r requirements.txt
pre-commit install
cd vue
npm install
cd ..
```
### Pushing the code to GitHub
- Create a GitHub repo (note: do not initialize the project with a readme): https://help.github.com/en/github/getting-started-with-github/create-a-repo
- At the top of your GitHub repository's Quick Setup page, click  to copy the remote repository URL. This will be `[GITHUB_URL]`
- Push the code to this repo:
```
git init
git add .
git commit -m "First commit"
git remote add origin [GITHUB_URL]
git remote -v
git push origin master
```

### Setting up the Heroku app
- Note: I recommend setting some env variables so that you can run things locally (any command starting with `setx`). The instructions below are for Windows, but setting variables is different on Mac/*nix
- Create the heroku app, and set the buildpacks:
 ```
heroku create [PROJECT_NAME]
heroku buildpacks:set heroku/python --app [PROJECT_NAME]
heroku buildpacks:add heroku/nodejs --app [PROJECT_NAME]
 ```
- **Note: all of the commands below provision free add-ons (as of writing). As your website scales, you may need to provision larger non-free versions.**
- Add logging:
```
heroku addons:create papertrail:choklad --app [PROJECT_NAME]
```
- Add database:
```
heroku addons:create heroku-postgresql:hobby-dev --app [PROJECT_NAME]
```
- Add sendgrid for sending emails and copy the environment variables locally:
```
heroku addons:create sendgrid:starter --app [PROJECT_NAME]
heroku config:get SENDGRID_USERNAME --app [PROJECT_NAME]  # This will print the username you want
setx SENDGRID_USERNAME [USERNAME_FROM_PREV_COMMAND]
heroku config:get SENDGRID_PASSWORD --app [PROJECT_NAME]  # This will print the password you want
setx SENDGRID_PASSWORD [PASSWORD_FROM_PREV_COMMAND]
```
- Add redis and amqp so that you can use celery for async tasks, and copy the environment variables locally:
```
heroku addons:create heroku-redis:hobby-dev --app [PROJECT_NAME]
heroku addons:create cloudamqp:lemur --app [PROJECT_NAME]
heroku config:get REDIS_URL --app [PROJECT_NAME]  # This will print the redis url you want
setx REDIS_URL [REDIS_URL_FROM_PREV_COMMAND]
heroku config:get CLOUDAMQP_URL --app [PROJECT_NAME]  # This will print the amqp url you want
setx CLOUDAMQP_URL [CLOUDAMQP_URL_FROM_PREV_COMMAND]
```
- Close and restart your command prompt so the env variables are updated

### Setting up the local postgres database
- Run the following commands to set some local variables
```
setx DJANGO_DB_NAME django_vue_db
setx DJANGO_DB_USER django_vue_user
setx DJANGO_DB_PWD [LOCAL_DB_PASSWORD]
```
- Open psql as the user postgres (password was set when you installed postgres, and IS NOT the password above) : `psql -U postgres`
- Once inside, run
```
CREATE DATABASE django_vue_db;
CREATE USER django_vue_user WITH PASSWORD '[LOCAL_DB_PASSWORD]';
GRANT ALL PRIVILEGES ON DATABASE django_vue_db TO django_vue_user;
\q
```

# License: MIT
