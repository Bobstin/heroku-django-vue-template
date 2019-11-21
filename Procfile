web: gunicorn {{ project_name }}.wsgi
celery: celery -A {{ project_name }} worker --loglevel info --without-heartbeat -Q default --hostname default-%h & celery -A {{ project_name }} beat --loglevel debug & wait -n
