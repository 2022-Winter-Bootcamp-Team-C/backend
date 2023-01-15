from django.urls import path
from . import views

urlpatterns = [
    path('list/<user_id>', views.get_income_list),
    path('new', views.post_new_income),
    path('<income_id>', views.put_new_Income),
    path('total_income/<user_id>', views.get_three_month_ago_income),
]