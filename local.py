import os
import sys
import click
import time
from subprocess import Popen

APP_NAME = 'django_vue'
DJANGO_COMMAND = ['python', 'manage.py', 'runserver']
NPM_COMMAND = ['npm', 'run', 'serve']
CELERY_WORKER_COMMAND = ['celery', '-A', APP_NAME, 'worker', '--loglevel', 'info', '--without-heartbeat', '-Q', 'default', '--hostname', 'default-%h']
CELERY_BEAT_COMMAND = ['celery', '-A', APP_NAME, 'beat', '--loglevel', 'debug']


@click.group()
def cli():
    pass


@cli.command()
@click.option('--django/--no-django', default=True)
@click.option('--npm/--no-npm', default=True)
@click.option('--celery/--no-celery', default=True)
def start(django, npm, celery):
    processes = []
    try:
        if django:
            processes.append(Popen(DJANGO_COMMAND, stdout=sys.stdout, stderr=sys.stderr))

        if npm:
            processes.append(Popen(NPM_COMMAND, stdout=sys.stdout, stderr=sys.stderr, cwd=os.getcwd() + '\\vue', shell=True))

        if celery:
            processes.append(Popen(CELERY_WORKER_COMMAND, stdout=sys.stdout, stderr=sys.stderr))
            processes.append(Popen(CELERY_BEAT_COMMAND, stdout=sys.stdout, stderr=sys.stderr))

        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Stopping all processes")
        for process in processes:
            process.terminate()


if __name__ == '__main__':
    cli()
