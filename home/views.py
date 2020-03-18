from django.shortcuts import render
from .models import Spending, Report
from django.views.generic import ListView
from .forms import ReportForm
from django.shortcuts import redirect


def home(request):
    return render(request, 'home/home.html')

class SpendingPlanListView(ListView):

    model = Spending
    template_name = 'home/home.html'
    context_object_name = 'spending_list'

def report_new(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
    else:
        form = ReportForm()
    if form.is_valid():
        report = form.save(commit=False)
        report.save()
        return redirect('report_table')
    return render(request, 'home/report_edit.html', {'form': form})

class ReportListView(ListView):

    model = Report
    template_name = 'home/report_table.html'
    context_object_name = 'report_list'

