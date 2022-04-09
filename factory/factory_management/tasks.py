from .models import Worker
from ..factory import celery_app
from .serializers import json_loader_for_seeder


@celery_app.task
def salary_pay():
    try:
        workers = json_loader_for_seeder(Worker.objects.all())
        for worker in workers:
            worker_data = Worker.objects.get(pk=worker['pk'])
            result_salary = worker['fields']['paid_salary'] +\
                            worker['fields']['salary']
            worker_data.update(paid_salary=result_salary)
    except Exception:
        print('Payment failed')


@celery_app.task
def async_info_update(queryset):
    queryset.update(paid_salary=0)
