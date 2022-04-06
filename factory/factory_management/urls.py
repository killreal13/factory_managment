from django.urls import path, re_path
from . import views


urlpatterns = [
    path('workers_data/', views.WorkersData.as_view()),
    re_path(r'^workers_data\/(\d)', views.SameLevelWorkersData.as_view())
]