from celery import Celery


# RUN CELERY - celery -A tasks.init_celery:celery worker --loglevel=INFO --pool=solo

celery = Celery(
    'tasks',
    broker='redis://localhost:6379',
    include=['tasks.ozon']
)

celery.conf.broker_connection_retry_on_startup = True
