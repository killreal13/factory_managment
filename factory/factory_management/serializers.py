from rest_framework import serializers
from django.core import serializers as json_serializer
import json


class WorkerDataSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=150)
    position = serializers.CharField(max_length=200)
    hiring_date = serializers.DateField()
    salary = serializers.DecimalField(decimal_places=2, max_digits=10)
    paid_salary = serializers.DecimalField(decimal_places=2, max_digits=10)


def json_loader_for_seeder(query_set):
    serialized_data = json_serializer.serialize('json', query_set)
    return json.loads(serialized_data)
