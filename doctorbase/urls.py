from django.urls import path
from doctorbase.views import index as home

urlpatterns = [
    path('', home, name='home')
]