from django.contrib import admin
from .models import Authority, Subject, Report

# Register your models here.
admin.site.register(Authority)
admin.site.register(Subject)
admin.site.register(Report)