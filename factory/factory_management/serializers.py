from rest_framework import serializers


class WorkerDataSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=150)
    position = serializers.CharField(max_length=200)
    hiring_date = serializers.DateField()
    salary = serializers.DecimalField(decimal_places=2, max_digits=10)
    paid_salary = serializers.DecimalField(decimal_places=2, max_digits=10)