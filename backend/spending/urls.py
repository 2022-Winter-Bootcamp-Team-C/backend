from django.urls import path
from . import views

app_name = 'api_spending'
urlpatterns = [
    path('spending/<user_id>', views.getSpendingdatas),
    path('spending/new/', views.postSendingdata),
    path('spending/total-cost/', views.totalSpendingcost),
]