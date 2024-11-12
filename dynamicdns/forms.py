from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from dynamicdns.models import DNSService, MonitoredRecord


class DNSServiceForm(forms.ModelForm):
    class Meta:
        model = DNSService
        fields = ('name', 'provider', 'auth_token')

    def __init__(self, *args, **kwargs):
        super(DNSServiceForm, self).__init__(*args, **kwargs)
        self.fields['provider'].required = False


class MonitoredRecordForm(forms.ModelForm):
    class Meta:
        model = MonitoredRecord
        fields = ('service', 'name', 'type', 'source_of_truth', 'dynamic_source_of_truth', 'interval')

    def __init__(self, *args, **kwargs):
        super(MonitoredRecordForm, self).__init__(*args, **kwargs)
        self.fields['service']=forms.ModelChoiceField(queryset=DNSService.objects.all())


# provider module specific forms
class CloudflareServiceForm(DNSServiceForm):
    """Cloudflare DNS Service Form"""
    zone_id = forms.CharField()



