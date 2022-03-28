from unicodedata import name
from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.add_file, name='add_file')
]
