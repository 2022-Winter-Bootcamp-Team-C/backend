from django.urls import path
from . import views

urlpatterns = [
    path('<user_id>', views.getincomeList),
    path('new/', views.postnewIncome)
]