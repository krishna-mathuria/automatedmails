from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ChooseTemplate, name='index'),
    path('/third', views.third, name='third')
]
