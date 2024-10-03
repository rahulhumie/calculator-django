from django.urls import path
from . import views
from .views import calculator

urlpatterns = [
    path('', views.calculator, name='calculator'),
]
