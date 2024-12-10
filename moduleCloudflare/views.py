from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from dns_providers import ProviderChoices
from dynamicdns.models import DNSService

from .forms import IndividualServiceForm

# Create your views here.
@login_required(login_url='login')
def new_individual_service(request):
    """
    Creates a new Service
    """
    context = {"request": request}
    if request.method == "GET":
        form = IndividualServiceForm()
        context['form'] = form

        context['provider_name'] = "Cloudflare"
        context['visible_fields'] = [("name", "Name"), ("auth_token", "API Key"), ("zone_id", "Zone ID")]

        return render(request, "forms/new_service.html", context)

    elif request.method == "POST":
        form = IndividualServiceForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            auth_token = form.cleaned_data['auth_token']
            zone_id = form.cleaned_data['zone_id']


            provider = ProviderChoices.CLOUDFLARE

            service_data = '{{"provider_name": "Cloudflare", "auth_token": "{0}", "zone_id": "{1}"}}'.format(auth_token,
                                                                                                             zone_id)

            DNSService.objects.create(name=name, provider=provider, auth_token=auth_token, service_data=service_data)

            return redirect('/')

        else:
            context['form'] = form
            return render(request, "forms/new_service.html", context)


@login_required(login_url='login')
def edit_individual_service(request):
    return None
