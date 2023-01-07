from django.template.defaulttags import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()
# router.register(r'posts', views.SpendingViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('new/', views.postSendingdata),
    path('purpose_ration/<user_id>', views.get_spending_rate_by_purpose),
    path('total_spending/<user_id>', views.get_spending_this_month),
    path('comparison_last_month/<user_id>', views.get_comparison_last_month),
    path('3month_sum/<user_id>', views.get_three_month_ago_spending),
    path('3month_avg/<user_id>', views.get_three_month_spending_average),
    path('spending-list/<user_id>', views.getSpendingdatas),
    path('<spending_id>', views.putSendingdata),
]
