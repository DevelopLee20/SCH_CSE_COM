from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('', views.info_main, name='main'),
]