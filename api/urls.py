from django.urls import re_path,path
from . import views

urlpatterns = [
    path('', views.getRoute, name='route'),
    path('users/', views.getUsers, name='users' ),
    path('users/diagnosis/', views.makeDiagnosis, name='diagnosis' ),
]