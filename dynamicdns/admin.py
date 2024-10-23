from django.contrib import admin
from .models import DNSService, MonitoredRecord

# Register your models here.
admin.site.register(DNSService)
admin.site.register(MonitoredRecord)
