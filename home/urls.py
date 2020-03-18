from django.urls import path
from . import views
from .views import SpendingPlanListView, ReportListView
urlpatterns = [
    path('', SpendingPlanListView.as_view(), name = 'home'),
    path('report/new/', views.report_new, name = 'report_new'),
    path('report_table/', ReportListView.as_view(), name = 'report_table'),

]