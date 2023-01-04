from django.urls import path
from . import views

app_name = 'api_spending'
urlpatterns = [
    path('', views.SpendingView.as_view()), #Spending에 관한 API를 처리하는 view로 Request를 넘김
]