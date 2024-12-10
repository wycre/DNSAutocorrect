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

        """
        Modify these context variables to adjust the APPEARANCE of the form
        visible_fields is a list of tuples containing the ("field_name", "Rendered Field Name")
            This is to allow you to rename fields in the rendered form.
            A FORM FIELD MUST BE INCLUDED IN THIS LIST TO BE RENDERED IN THE FORM PAGE
        """
        context['provider_name'] = "template"
        context['visible_fields'] = [("name", "Name"), ("auth_token", "API Key")]

        return render(request, "forms/new_service.html", context)

    elif request.method == "POST":
        form = IndividualServiceForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            auth_token = form.cleaned_data['auth_token']
            zone_id = form.cleaned_data['zone_id']

            """
            MODIFY this ProviderChoice to match the the provider being added.
            """
            provider = ProviderChoices.CLOUDFLARE

            """
            MODIFY this formatted string to match the expected format for the UPA functions
            """
            service_data = '{{"provider_name": "template", "auth_token": "{0}", "zone_id": "{1}"}}'.format(auth_token,
                                                                                                             zone_id)

            DNSService.objects.create(name=name, provider=provider, auth_token=auth_token, service_data=service_data)

            return redirect('/')

        else:
            context['form'] = form
            return render(request, "forms/new_service.html", context)


@login_required(login_url='login')
def edit_individual_service(request):
    return None

@login_required(login_url='login')
def delete_individual_service(request):
    return None
