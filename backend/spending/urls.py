from django.urls import path, include
from . import views

urlpatterns = [
    path('spending/<user_id>', views.getSpendingdatas),
    path('spending/new/', views.postSendingdata),
    path('spending/total-cost/', views.totalSpendingcost),
]