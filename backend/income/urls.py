from django.urls import path
from . import views

urlpatterns = [
    path('<user_id>', views.get_income_list),
    path('new/', views.post_new_income),
    path('total_income/<user_id>', views.get_income_this_month),
]