from django.db import models
#from django.contrib.gis.db import models
from django.urls import reverse

# Create your models here.
class Authority(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title 

class Subject(models.Model):
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.subject


class Report( models.Model):    
    recipient = models.ForeignKey(Authority, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    occurrence_date = models.DateTimeField(auto_now_add=True)
    report_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    reporter_ip = models.CharField(max_length=200, null=True)
    reporter_lat = models.CharField(max_length=200, null=True)
    reporter_long = models.CharField(max_length=200, null=True)
    evidence_file = models.FileField(blank=True, null=True)
    #location = models.PointField()

    def __str__(self):
        return str(self.recipient)

    def get_absolute_url(self):
        return reverse('report-list')
