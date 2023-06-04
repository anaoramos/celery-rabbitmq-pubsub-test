"""
Celery setup.
"""
from celery import Celery

app = Celery("app")
app.config_from_object('celeryconfig')
