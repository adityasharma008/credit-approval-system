import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "credit_approval_system.settings")

celery_app = Celery("credit_approval_system")

celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()