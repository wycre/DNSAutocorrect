from django.db import models
from dns_providers import Providers, PROVIDER_MAPPINGS


# Create your models here.
class DNSService(models.Model):
    """
    Defines a DNS service provider that is in use.
    Requires a reference to an existing DNS provider module, and an auth key.
    """
    name = models.CharField(max_length=255, blank=True)
    provider = models.CharField(max_length=255, blank=False, choices=PROVIDER_MAPPINGS)
    auth_token = models.TextField(blank=False)
    str1 = models.TextField(blank=True)  # Fields utilized by provider requirements
    str2 = models.TextField(blank=True)


class MonitoredRecord(models.Model):
    """
    Defines a monitored DNS record.
    name refers to the record name, and is therefore required.
    source_of_truth holds the staticly assigned IP address, if applicable.
    dynamic_source_of_truth determines whether to use dynamic DNS or static assignment.
    history holds the most recently authorized record value (last set by this software)
    service refers to the DNS service that this record belongs to.
    """
    name = models.CharField(max_length=255, blank=False)
    source_of_truth = models.CharField(max_length=255, blank=True)
    dynamic_source_of_truth = models.BooleanField(default=True)
    history = models.TextField(blank=True)
    service = models.ForeignKey(DNSService, on_delete=models.CASCADE)

