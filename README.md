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
In the instructions below, replace anything in square brackets `[]` with whatever you choose.
Note that [{{ project_name }}] should meet the Heroku and GitHub name requirements: name must start with a letter, end with a letter or digit and can only contain lowercase letters, digits, and dashes.

To use this project, follow these steps:

### Create the initial environment
- Create the environment (I recommend conda): `conda create -n [{{ project_name }}]env python=3.6`
- Activate that environment: `activate [{{ project_name }}]env`
- Install Django: `pip install django`

### Create your project and install the requirements

- Create the template in the local directory
```
django-admin.py startproject --template=https://github.com/Bobstin/heroku-django-vue-template/archive/master.zip --name=Procfile,app.json [{{ project_name }}]
cd [{{ project_name }}]
```
(If this doesn't work on windows, replace `django-admin.py` with `django-admin`)

### Push the code to GitHub
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

### Install the requirements:
```
pip install -r requirements.txt
pre-commit install
cd vue
npm install
cd ..
```

### Set up the Heroku app
- Create the heroku pipeline, answering the questions as desired. I recommend deploying master to staging, enabling review apps, and creating a review app for each PR. CI is also helpful, but note that Heroku charges $10/month for the service. This will create the staging and production apps automatically, including add-ons.
 ```
heroku pipelines:setup [{{ project_name }}]
 ```
At this point, you should be able to see the test app at `https://[{{ project_name }}].herokuapp.com/`
- Copy some key environment variables locally. The first command in each pair will print a value, which you set locally via the second command. Note: The instructions below are for Windows, but setting variables is different on Mac/*nix
```
heroku config:get SENDGRID_USERNAME
setx SENDGRID_USERNAME [USERNAME_FROM_PREV_COMMAND]

heroku config:get SENDGRID_PASSWORD
setx SENDGRID_PASSWORD [PASSWORD_FROM_PREV_COMMAND]

heroku config:get REDIS_URL
setx REDIS_URL [REDIS_URL_FROM_PREV_COMMAND]

heroku config:get CLOUDAMQP_URL
setx CLOUDAMQP_URL [CLOUDAMQP_URL_FROM_PREV_COMMAND]
```
- Close and restart your command prompt so the env variables are updated

### Set up the local postgres database
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
- Close and restart your command prompt so the env variables are updated

## Running the app
To make it easier to run all of the processes required for this template, a custom command called `run_local` is added to `manage.py`.
Note that node will report the app is running on port 8080 - this is not correct. Pay attention to where django is serving the app (`http://127.0.0.1:8000/`).

It will start the following processes:
- The django local server (`python manage.py runserver`); can be turned of with the `--no-django` flag
- Node, including hot reloading! (`npm run serve`); can be turned of with the `--no-npm` flag
- A celery worker (`celery -A [{{ project_name }}] worker --loglevel info --without-heartbeat -Q default --hostname default-%h`); can be turned of with the `--no-celery` flag
- Celery beat (`celery -A [{{ project_name }}] beat --loglevel debug`); can be turned of with the `--no-celery` flag

You can run it with `python manage.py run_local`; see the flags above if you don't want all of the processes.

If you want to extend it, the script can be found in `example_app/management/commands/run_local.py`. Note that if you want to delete the example app, you should put this file in the same sub-directory but in the new app. 
# License: MIT
