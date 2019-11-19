import os
import sys
import click
import time
from subprocess import Popen

DJANGO_COMMAND = ['python', 'manage.py', 'runserver']
NPM_COMMAND = ['npm', 'run', 'serve']


@click.group()
def cli():
    pass


@cli.command()
@click.option('--django/--no-django', default=True)
@click.option('--npm/--no-npm', default=True)
def start(django, npm):
    processes = []
    try:
        if django:
            processes.append(Popen(DJANGO_COMMAND, stdout=sys.stdout, stderr=sys.stderr))

        if npm:
            processes.append(Popen(NPM_COMMAND, stdout=sys.stdout, stderr=sys.stderr, cwd=os.getcwd() + '\\vue', shell=True))

        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Stopping all processes")
        for process in processes:
            process.terminate()


if __name__ == '__main__':
    cli()
