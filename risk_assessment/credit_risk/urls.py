from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns=[
    path('index',views.index),
    path('loan_status',views.loan_status),
]