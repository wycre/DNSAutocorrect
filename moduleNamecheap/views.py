from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from dns_providers import ProviderChoices
from dynamicdns.models import DNSService

from .forms import NamecheapServiceForm

# Create your views here.
@login_required(login_url='login')
def new_namecheap_service(request):
    context = {"request": request}
    if request.method == "GET":
        form = NamecheapServiceForm()
        context['form'] = form
        context['provider_name'] = "Namecheap"
        context['visible_fields'] = [("name", "Name"), ("auth_token", "API Key"), ("zone_id", "Zone ID"), ("zone_name", "Zone Name")]

        return render(request, "forms/new_service.html", context)

    elif request.method == "POST":
        form = NamecheapServiceForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            auth_token = form.cleaned_data['auth_token']
            zone_id = form.cleaned_data['zone_id']
            zone_name = form.cleaned_data['zone_name']
            provider = ProviderChoices.NAMECHEAP

            service_data = '{{"provider_name": "Namecheap", "auth_token": "{0}", "zone_id": "{1}", "zone_name": "{2}"}}'.format(auth_token,
                                                                                                             zone_id, zone_name)

            DNSService.objects.create(name=name, provider=provider, auth_token=auth_token, service_data=service_data)

            return redirect('/')

        else:
            context['form'] = form
            return render(request, "forms/new_service.html", context)

@login_required(login_url='login')
def edit_namecheap_service(request):
    return None

