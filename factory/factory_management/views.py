from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import permissions
from .models import *
from .serializers import WorkerDataSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin


class WorkersData(APIView, PermissionRequiredMixin):
    def get(self, request):
        print(request.user.has_perm('kek'))
        queryset = Worker.objects.all()
        serializer_for_queryset = WorkerDataSerializer(instance=queryset, many=True)
        if queryset:
            return Response(serializer_for_queryset.data)
        return Response(status=204)


class SameLevelWorkersData(APIView):
    def get(self, request, worker_level=1):
        queryset = Worker.objects.all().filter(level=worker_level)
        serializer_for_queryset = WorkerDataSerializer(instance=queryset, many=True)
        if queryset:
            return Response(serializer_for_queryset.data)
        return Response(status=204)
