from django.urls import path
from . import views
from .views import SpendingPlanListView, ReportListView,SummaryListView
urlpatterns = [
    path('', SpendingPlanListView.as_view(), name = 'home'),
    path('report/new/', views.report_new, name = 'report_new'),
    path('summary/new/', views.summary_new, name = 'summary_new'),
    path('report_table/', ReportListView.as_view(), name = 'report_table'),
    path('summary_table/', SummaryListView.as_view(), name = 'summary_table'),

]