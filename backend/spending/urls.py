from django.template.defaulttags import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import get_spending_datas

# router = DefaultRouter()
# router.register(r'posts', views.SpendingViewSet)

urlpatterns = [
    path('spending-list/<user_id>', views.get_spending_datas),  # B-1
    path('new/', views.post_spending_data),  # B-2
    path('<id>', views.put_delete_data),  # B-3
    path('purpose_ration/<user_id>', views.get_spending_rate_by_purpose),  # D-1
    path('total_spending/<user_id>', views.get_spending_this_month),  # D-2
    path('comparison_last_month/<user_id>', views.get_comparison_last_month),  # D-4
    path('3month_sum/<user_id>', views.get_three_month_ago_spending),  # D-6
    path('spending_income_ratio/<user_id>', views.get_spending_income_ratio_this_month),  # D-7
    path('3month_spending_income_ratio/<user_id>', views.get_spending_income_ratio_3month),  # D-8
    # path('', include(router.urls)),
    # path('3month_avg/<user_id>', views.get_three_month_spending_average),
    # path('spending-list/<user_id>', get_spending_datas.views),
]
