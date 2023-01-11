from django.urls import path, include
from . import views

urlpatterns = [
    # path('new', views.registration),
    path('new', views.join),
    path('login', views.login),
]
