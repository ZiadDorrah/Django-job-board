from django.contrib import admin
from django.urls import path, include
from .models import job_list, job_detail
urlpatterns = [
    path('', views.job_list),
    path('<int:id> ', views.job_detail),
]
