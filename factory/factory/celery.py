# import os
# from celery import Celery
# from celery.schedules import crontab
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_task.settings')
# app = Celery('celery_task')
# app.congif_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
# app.conf.beat_schedule = {
#     'task_name': {
#         'task': 'path_to_func',
#         'schedule': crontab(minute=59, hour='*/1')
#     }
# }
