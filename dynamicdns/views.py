from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


from django.urls import reverse_lazy
from django.views.generic import CreateView


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from dynamicdns.models import DNSService, MonitoredRecord
from .forms import MonitoredRecordForm
from .tasks import run_dns_engine

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
    context["records"] = MonitoredRecord.objects.all()

    return render(request, "index.html", context)


@login_required(login_url='login')
def run_dns_check(request):
    """
    Manually runs dns check.
    """
    if request.method == "GET":
        return redirect("/")
    elif request.method == "POST":
        run_dns_engine()
        return redirect("/")


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
            service = form.cleaned_data['service']
            history = ""

            record = MonitoredRecord.objects.create(name=name, type=type, source_of_truth=sot,
                                                    dynamic_source_of_truth=dynamic_sot,
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

