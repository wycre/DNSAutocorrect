from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import json
import inspect
from cron_validator import CronValidator

from django.urls import reverse_lazy
from django.views.generic import CreateView

import dynamicdns.dns_providers as dns_providers
from django.http import HttpResponse
from django import forms
from .decorators import unauthenticated, allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from dynamicdns.models import DNSService, MonitoredRecord, RecordTypes
from .forms import MonitoredRecordForm, CloudflareServiceForm

def index(request):

    # GUARD: If no users detected, redirect to setup
    users = User.objects.all()
    if len(users) == 0:
        return redirect('setup')

    # GUARD: Ensure user is logged in
    if not request.user.is_authenticated:
        return redirect('login')


    # Build Test Index Data
    context = {"request": request}

    context["services"] = DNSService.objects.all()

    service = DNSService.objects.all()[0]
    context["test_service"] = service
    service_data = json.loads(service.service_data)
    context["service_data"] = service_data

    service_methods = []
    service_methods_raw = dns_providers.upa_resolver(service.provider)
    service_methods.append(inspect.getsourcefile(service_methods_raw[0]))
    service_methods.append(inspect.getsourcefile(service_methods_raw[1]))
    context["service_methods"] = service_methods

    context["monitored_records"] = MonitoredRecord.objects.all()

    return render(request, "index.html", context)

class SetUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/setup.html"


"""
Record Forms
"""
@login_required(login_url='login')
def new_monitored_record(request):
    context = {"request": request}

    if request.method == "GET":
        form = MonitoredRecordForm()
        context['form'] = form
        context['services'] = DNSService.objects.all()
        return render(request, "forms/new_monitored_record.html", context)

    elif request.method == "POST":
        form = MonitoredRecordForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            type = form.cleaned_data['type']
            sot = form.cleaned_data['source_of_truth']
            dynamic_sot = form.cleaned_data['dynamic_source_of_truth']
            interval = form.cleaned_data['interval']
            service = form.cleaned_data['service']
            history = ""

            # Validate Interval
            try:
                v_interval = CronValidator.parse(interval)
            except ValueError:
                form.add_error("interval",
                               'Invalid <a href="https://crontab.cronhub.io/" target="_blank">Cron</a> Expression')
                context['form'] = form
                return render(request, "forms/new_monitored_record.html", context)




            record = MonitoredRecord.objects.create(name=name, type=type, source_of_truth=sot,
                                                    dynamic_source_of_truth=dynamic_sot, interval=interval,
                                                    service=service, history=history)

            context['record'] = record
            return redirect('/')

        else:
            context['form'] = form
            return render(request, "forms/new_monitored_record.html", context)

@login_required(login_url='login')
def edit_monitored_record(request):
    return None

@login_required(login_url='login')
def delete_monitored_record(request):
    return None


"""
Service Forms
"""
@login_required(login_url='login')
def new_service_chooser(request):
    """Displays a page allowing the user to pick the service provider"""
    context = {"request": request}
    return render(request, "new_service_chooser.html", context)


"""Cloudflare"""
@login_required(login_url='login')
def new_cloudflare_service(request):
    context = {"request": request}
    if request.method == "GET":
        form = CloudflareServiceForm()
        context['form'] = form
        context['provider_name'] = "Cloudflare"
        context['visible_fields'] = [("name", "Name"), ("auth_token", "API Key"), ("zone_id", "Zone ID")]

        return render(request, "forms/new_service.html", context)

    elif request.method == "POST":
        form = CloudflareServiceForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            auth_token = form.cleaned_data['auth_token']
            zone_id = form.cleaned_data['zone_id']
            provider = dns_providers.ProviderChoices.CLOUDFLARE

            service_data = '{{"provider_name": "Cloudflare", "auth_token": "{0}", "zone_id": "{1}"}}'.format(auth_token,
                                                                                                             zone_id)

            DNSService.objects.create(name=name, provider=provider, auth_token=auth_token, service_data=service_data)

            return redirect('/')

        else:
            context['form'] = form
            return render(request, "forms/new_service.html", context)

@login_required(login_url='login')
def edit_cloudflare_service(request):
    return None

@login_required(login_url='login')
def delete_cloudflare_service(request):
    return None


"""Namecheap"""
@login_required(login_url='login')
def new_namecheap_service(request):
    pass

@login_required(login_url='login')
def edit_namecheap_service(request):
    return None

@login_required(login_url='login')
def delete_namecheap_service(request):
    return None
