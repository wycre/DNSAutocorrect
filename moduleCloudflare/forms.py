from django import forms
from dynamicdns.forms import DNSServiceForm

class CloudflareServiceForm(DNSServiceForm):
    zone_id = forms.CharField()
