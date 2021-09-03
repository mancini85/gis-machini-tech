from django import forms
from . models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('recipient', 'subject', 'description', 'evidence_file')

        widgets = {
        	'recipient': forms.Select(attrs={'class': 'form-control'}),
        	'subject': forms.Select(attrs={'class': 'form-control'}),
        	'description': forms.TextInput(attrs={'class': 'form-control'}),
        	'evidence_file': forms.Select(attrs={'class': 'form-control'}),
        	#'location': forms.Select(attrs={'class': 'form-control'}),
        }
