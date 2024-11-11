from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from dynamicdns.models import DNSService, MonitoredRecord


class DNSServiceForm(forms.ModelForm):
    class Meta:
        model = DNSService
        fields = ('name', 'provider', 'auth_token')


class MonitoredRecordForm(forms.ModelForm):
    class Meta:
        model = MonitoredRecord
        fields = ('service', 'name', 'source_of_truth', 'dynamic_source_of_truth')

    def __init__(self, *args, **kwargs):
        super(MonitoredRecordForm, self).__init__(*args, **kwargs)
        self.fields['service']=forms.ModelChoiceField(queryset=DNSService.objects.all())

