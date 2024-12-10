from django import forms
from dynamicdns.forms import DNSServiceForm

class IndividualServiceForm(DNSServiceForm):
    zone_id = forms.CharField()
