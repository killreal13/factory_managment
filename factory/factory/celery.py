import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_task.settings')
app = Celery('celery_task')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'update_paid_salary_data_every_hour': {
        'task': 'factory_management.tasks.salary_pay',
        'schedule': crontab(minute=59, hour='*/1')
    }
}
