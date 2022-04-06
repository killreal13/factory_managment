from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import *
from .serializers import WorkerDataSerializer


class WorkersData(APIView):
    def get(self, request):
        queryset = Worker.objects.all()
        serializer_for_queryset = WorkerDataSerializer(instance=queryset, many=True)
        return Response(serializer_for_queryset.data)


class SameLevelWorkersData(APIView):
    pass
