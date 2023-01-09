from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('list/<user_id>', views.getincomeList),
=======
    path('<user_id>', views.getincomeList),
>>>>>>> main
    path('new/', views.postnewIncome),
    path('<income_id>', views.putnewIncome)
]