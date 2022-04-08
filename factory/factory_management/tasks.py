# from .models import Worker
# from ..factory import celery
# from .serializers import json_loader_for_seeder
#
#
# @celery.app.task
# def salary_pay(user_name: str):
#     try:
#         worker = Worker.objects.get(username=user_name)
#         result_salary = json_loader_for_seeder(worker)['paid_salary'] + json_loader_for_seeder(worker)['salary']
#         worker.update(paid_salary=result_salary)
#     except Exception:
#         print('Payment failed')
