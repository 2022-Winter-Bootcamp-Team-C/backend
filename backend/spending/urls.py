from django.template.defaulttags import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()
# router.register(r'posts', views.SpendingViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('spending/<user_id>', views.getSpendingdatas),
    path('spending/new/', views.postSendingdata),
    path('spending/total-cost/', views.totalSpendingcost),
    path('spending/purpose_ration/<user_id>', views.get_spending_rate_by_purpose),
    path('spending/total_spending/<user_id>', views.get_spending_this_month),
    path('spending/comparison_last_month/<user_id>', views.get_comparison_last_month),
]