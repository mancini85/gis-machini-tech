from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
#from models import Regions, Counties, SubCounties, Constituencies, Wards, Locations, SubLocations, Incidences
from .models import Authority, Subject, Report
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from .forms import ReportForm
from django.urls import reverse_lazy
# Create your views here.
def report(request):
	return render(request, 'reporter/report.html')

#Report views
class AuthorityCreateView(CreateView):
    model = Authority
    template_name = 'reporter/authority.html'
    success_url = 'authority_list'


class SubjectCreateView(CreateView):
    model = Subject
    template_name = 'reporter/subject.html'
    success_url = 'subject_list'

class AuthorityView(ListView):
    model = Authority

class SubjectView(ListView):
    model = Subject
class ReportView(ListView):
    model = Report
    template_name = "reporter/report_list.html"



class AuthorityDeleteView(DeleteView):
    model = Authority
    success_url = reverse_lazy('authority_list')

class SubjectDeleteView(DeleteView):
    model = Subject
    success_url = reverse_lazy('subject_list')

class ReportDeleteView(DeleteView):
    model = Report
    success_url = reverse_lazy('subject_list')
    
class ReportSomething(CreateView):
    model = Report
    #fields = "__all__"
    form_class = ReportForm
    template_name = "reporter/report_something.html"
    success_url = reverse_lazy('report-list')
