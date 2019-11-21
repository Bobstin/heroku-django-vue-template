from {{ project_name }}.celery import app
from datetime import datetime


@app.task(queue="default")
def example_task(message):
    print(f'I am inside a celery task. The message I received was: {message}')


@app.task(queue="default")
def example_beat_task():
    print(f'I am inside a celery task being called by celery beat. The the current time is {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
