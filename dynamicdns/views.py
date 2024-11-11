from django.shortcuts import render
import json
import inspect
import dynamicdns.dns_providers as dns_providers
from django.http import HttpResponse
from django import forms
from .decorators import unauthenticated, allowed_users
from django.contrib.auth.decorators import login_required

from dynamicdns.models import DNSService, MonitoredRecord, RecordTypes
from .forms import MonitoredRecordForm


# from dynamicdns.forms import


# Create your views here.
def index(request):
    service = DNSService.objects.all()[0]
    service_data = json.loads(service.service_data)

    service_methods = []
    service_methods_raw = dns_providers.upa_resolver(service.provider)
    service_methods.append(inspect.getsourcefile(service_methods_raw[0]))
    service_methods.append(inspect.getsourcefile(service_methods_raw[1]))
    print(service_methods)


    return render(request, "index.html", {"request": request, "service": service, "service_data": service_data, "service_methods": service_methods})

def new_monitored_record(request):
    context = {"request": request}

    if request.method == "GET":
        form = MonitoredRecordForm()
        context['form'] = form
        context['services'] = DNSService.objects.all()
        return render(request, "forms/new_monitored_record.html", context)
