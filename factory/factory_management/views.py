from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import WorkerDataSerializer
from .check_permission_existence import PermissionChecker
from .check_group_existence import GroupChecker


AVAILABLE_POSITIONS = ['CEO', 'MMM', 'MM']


class WorkersData(APIView):
    def get(self, request):
        permission = PermissionChecker('can_use_apis', 'Can use APIs').check(Worker)
        group_with_access = GroupChecker('Can use APIs').check(permission)
        queryset = Worker.objects.all()
        serializer_for_queryset = WorkerDataSerializer(instance=queryset, many=True)
        ordered_user_data = [value for value in serializer_for_queryset.data[0].items()]
        user_data = {key: value for key, value in ordered_user_data}
        for position in AVAILABLE_POSITIONS:
            if user_data['position'] == position:
                request.user.groups.add(group_with_access)
        if not request.user.has_perm('Can use APIs'):
            return Response(status=423)
        if queryset:
            return Response(serializer_for_queryset.data)
        return Response(status=204)


class SameLevelWorkersData(APIView):
    def get(self, request, worker_level=1):
        permission = PermissionChecker('can_use_apis', 'Can use APIs').check(Worker)
        group_with_access = GroupChecker('Can use APIs').check(permission)
        queryset = Worker.objects.all().filter(level=worker_level)
        serializer_for_queryset = WorkerDataSerializer(instance=queryset, many=True)
        ordered_user_data = [value for value in serializer_for_queryset.data[0].items()]
        user_data = {key: value for key, value in ordered_user_data}
        for position in AVAILABLE_POSITIONS:
            if user_data['position'] == position:
                request.user.groups.add(group_with_access)
        if not request.user.has_perm('Can use APIs'):
            return Response(status=423)
        if queryset:
            return Response(serializer_for_queryset.data)
        return Response(status=204)
