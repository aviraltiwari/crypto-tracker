import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trackerApi.settings')

app = Celery('trackerApi')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
