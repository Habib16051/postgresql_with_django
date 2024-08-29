from django.urls import path, include
from pdjango import views

urlpatterns = [
    path('', views.home, name='home'),
]
