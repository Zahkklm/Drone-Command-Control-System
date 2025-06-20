from django.urls import path
from .views import DashboardSummaryView, dashboard_summary_page

urlpatterns = [
    path('summary/', DashboardSummaryView.as_view(), name='dashboard-summary'),
    path('', dashboard_summary_page, name='dashboard-summary-page'),
]