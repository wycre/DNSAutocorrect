from django.db import models
from .dns_providers import Providers, ProviderChoices


class RecordTypes(models.TextChoices):
    A = "1", "A - IPv4"
    AAAA = "2", "AAAA - IPv6"


# Create your models here.
class DNSService(models.Model):
    """
    Defines a DNS service provider that is in use.
    Requires a reference to an existing DNS provider module, and an auth key.
    """
    name = models.CharField(max_length=255, blank=False)
    provider = models.CharField(max_length=255, blank=False, choices=ProviderChoices)
    auth_token = models.TextField(blank=False)
    service_data = models.TextField(blank=False)  # JSON object that is only compatible with specific providers

    def __str__(self):
        return self.name



class MonitoredRecord(models.Model):
    """
    Defines a monitored DNS record.
    name refers to the record name, and is therefore required.
    source_of_truth holds the staticly assigned IP address, if applicable.
    dynamic_source_of_truth determines whether to use dynamic DNS or static assignment.
    interval holds a cron expression that determines how often the DNS record is checked
    history holds the most recently authorized record value (last set by this software)
    service refers to the DNS service that this record belongs to.
    """
    # User Provided Data
    name = models.CharField(max_length=255, blank=False)
    type = models.CharField(max_length=255, blank=False, choices=RecordTypes, default=RecordTypes.A)
    source_of_truth = models.CharField(max_length=255, blank=True)
    dynamic_source_of_truth = models.BooleanField(default=True)
    interval = models.CharField(max_length=255, blank=False, default='* * * * *')
    service = models.ForeignKey(DNSService, on_delete=models.CASCADE)

    # Internal Use Data
    history = models.TextField(blank=True)


    def __str__(self):
        return self.name

