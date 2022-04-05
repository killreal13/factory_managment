from django.db import models
from django.contrib.auth.models import User


class Position(models.Model):
    name = models.CharField(choices=[
        ('CEO', 'CEO'),
        ('MMM', 'Middle manager manager'),
        ('MM', 'Middle manager'),
        ('SM', 'Subordinate manager'),
        ('SW', 'Simple worker')
    ])


class Worker(models.Model):
    id = models.UUIDField(default=True, null=False, blank=False)
    user = models.OneToManyField(User, null=False, blank=False, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150, null=False, blank=False)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, blank=True, null=True)
    hiring_date = models.DateField(default=True, null=False, blank=False)
    salary = models.DecimalField(null=False, blank=False)
    paid_salary = models.DecimalField(null=False, blank=False)
