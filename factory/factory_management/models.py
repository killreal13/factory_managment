from django.db import models
from django.contrib.auth.models import User


class Worker(models.Model):
    worker_id = models.AutoField(primary_key=True)
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


class WorkerRelation(models.Model):
    head = models.ForeignKey(Worker, null=True, blank=False, on_delete=models.CASCADE, related_name='head_of_workers')
    secondary = models.ForeignKey(Worker, null=True, blank=False, on_delete=models.CASCADE, related_name='secondary_workers')
