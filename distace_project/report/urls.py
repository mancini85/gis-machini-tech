from django.conf.urls import include,url
from django.urls import path
from . import views
from .views import AuthorityCreateView, SubjectCreateView, ReportSomething
from .views import AuthorityView, SubjectView, ReportView 
from .views import AuthorityDeleteView, SubjectDeleteView, ReportDeleteView
"""
from views import HomePageView, county_datasets,point_datasets

urlpatterns = [
	url(r'^$', HomePageView.as_view(), name = 'home'),
	url(r'^county_data/$', county_datasets, name = 'county'),
	url(r'^incidence_data/$', point_datasets, name = 'incidences'),


] 
"""

urlpatterns = [
    path("report-something/", ReportSomething.as_view(), name="report-something"),

    #Create Urls
    path("create_authority/", AuthorityCreateView.as_view(), name="create_authority"),
    path("create_subject/", SubjectCreateView.as_view(), name="create_subject"),

 
    #Update Urls
    path("authority_list", AuthorityView.as_view(), name="authority_list"),
    path("subject_list", SubjectView.as_view(), name="subject_list"),
    path("report-list", ReportView.as_view(), name="report-list"),


    path("<pk>/delete", AuthorityDeleteView.as_view(), name="delete_authority"),
    path("<pk>/delete", SubjectDeleteView.as_view(), name="delete_subject"),
    path("<pk>/delete", ReportDeleteView.as_view(), name="delete_report"),
]