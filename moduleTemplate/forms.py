from django import forms
from dynamicdns.forms import DNSServiceForm

class IndividualServiceForm(DNSServiceForm):
    """
    MODIFY this class to add new fields as needed, then remove the `pass` line
    i.e. zone_id = forms.CharField()
    """
    pass
