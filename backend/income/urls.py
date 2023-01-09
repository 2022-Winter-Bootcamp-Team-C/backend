from django.urls import path
from . import views

urlpatterns = [
    path('list/<user_id>', views.getincomeList),
    path('new/', views.postnewIncome),
    path('<income_id>', views.putnewIncome)
]