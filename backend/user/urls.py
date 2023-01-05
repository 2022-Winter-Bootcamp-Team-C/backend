from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.join),
    # path('login', views.login),
]