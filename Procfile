web: gunicorn django_vue.wsgi
celery: celery -A django_vue worker --loglevel info --without-heartbeat -Q default --hostname default-%h
celery_beat: celery -A django_vue beat --loglevel debug
