from django.template.defaulttags import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()
# router.register(r'posts', views.SpendingViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('new/', views.post_spending_data),
    path('purpose_ration/<user_id>', views.get_spending_rate_by_purpose),
    path('total_spending/<user_id>', views.get_spending_this_month),
    path('comparison_last_month/<user_id>', views.get_comparison_last_month),
    path('3month_sum/<user_id>', views.get_three_month_ago_spending),
    path('spending-list/<user_id>', views.get_spending_datas),
    path('<spending_id>', views.put_spending_data),
    path('d/<spending_id>', views.delete_spending_data),
]
