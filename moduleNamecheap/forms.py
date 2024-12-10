from django import forms
from dynamicdns.forms import DNSServiceForm

class NamecheapServiceForm(DNSServiceForm):
    zone_id = forms.CharField()
    zone_name = forms.CharField()
