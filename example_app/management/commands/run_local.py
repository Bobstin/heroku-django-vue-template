import os
import sys
import time
from subprocess import Popen

from django.core.management.base import BaseCommand

APP_NAME = '{{ project_name }}'
DJANGO_COMMAND = ['python', 'manage.py', 'runserver']
NPM_COMMAND = ['npm', 'run', 'serve']
CELERY_WORKER_COMMAND = ['celery', '-A', APP_NAME, 'worker', '--loglevel', 'info', '--without-heartbeat', '-Q', 'default', '--hostname', 'default-%h']
CELERY_BEAT_COMMAND = ['celery', '-A', APP_NAME, 'beat', '--loglevel', 'debug']


class Command(BaseCommand):
    help = "Runs the processes required for the website locally"

    def add_arguments(self, parser):
        parser.add_argument('--no-django', action='store_false', help='Do not start the django process', dest='django')
        parser.add_argument('--no-npm', action='store_false', help='Do not start the npm process', dest='npm')
        parser.add_argument('--no-celery', action='store_false', help='Do not start the celery beat and worker processes', dest='celery')

    def handle(self, *args, **kwargs):
        django = kwargs['django']
        npm = kwargs['npm']
        celery = kwargs['celery']

        processes = []
        try:
            if django:
                processes.append(Popen(DJANGO_COMMAND, stdout=sys.stdout, stderr=sys.stderr))

            if npm:
                processes.append(
                    Popen(NPM_COMMAND, stdout=sys.stdout, stderr=sys.stderr, cwd=os.getcwd() + '\\vue', shell=True))

            if celery:
                processes.append(Popen(CELERY_WORKER_COMMAND, stdout=sys.stdout, stderr=sys.stderr))
                processes.append(Popen(CELERY_BEAT_COMMAND, stdout=sys.stdout, stderr=sys.stderr))

            while True:
                time.sleep(10)
        except KeyboardInterrupt:
            print("Stopping all processes")
            for process in processes:
                process.terminate()
