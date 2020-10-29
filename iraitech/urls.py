from django.urls import path
from . import views

urlpatterns = [
    path('', views.question1, name="question1"),
    path('api/v1/calculate', views.calculate, name="calculate")
]
