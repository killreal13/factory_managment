from django.db import models
import uuid
from django.contrib.auth.models import User


# class Position(models.Model):
#     name = models.CharField(max_length=200, choices=[
#         ('CEO', 'CEO'),
#         ('MMM', 'Middle manager manager'),
#         ('MM', 'Middle manager'),
#         ('SM', 'Subordinate manager'),
#         ('SW', 'Simple worker')
#     ], default='SW')


class Worker(models.Model):
    worker_id = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid.uuid4())
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150, null=False, blank=False)
    position = models.CharField(max_length=200, choices=[
        ('CEO', 'CEO'),
        ('MMM', 'Middle manager manager'),
        ('MM', 'Middle manager'),
        ('SM', 'Subordinate manager'),
        ('SW', 'Simple worker')
    ], default='SW')
    level = models.IntegerField(null=True, blank=True)
    hiring_date = models.DateField(null=False, blank=False)
    salary = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=10)
    paid_salary = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=10)

    @property
    def get_head(self):
        return WorkerRelation.objects.get(secondary=self.worker_id)

    class Meta:
        permissions = [('kek', 'kek'),]


    # @property
    # def get_s(self):
    #     return WorkerRelation.objects.get(secondary=self.worker_id)
    # def __str__(self):
    #     head = WorkerRelation.objects.all().filter(secondary=self.worker_id).values('head')
    #     return self.full_name, self.position, head


# class Payments(models.Model):
#     payment_id = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid.uuid4())
#     worker_id = models.ForeignKey(Workers, on_delete=models.CASCADE, null=False, blank=False)
#     payment_size = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=10)

class WorkerRelation(models.Model):
    head = models.ForeignKey(Worker, null=True, blank=True, on_delete=models.CASCADE, related_name='head_of_workers')
    secondary = models.ForeignKey(Worker, null=True, blank=True, on_delete=models.CASCADE, related_name='secondary_workers')
