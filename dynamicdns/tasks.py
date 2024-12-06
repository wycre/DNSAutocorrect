"""
Celery tasks for dynamicdns.
"""

from celery import shared_task
from requests import get
import dynamicdns.dns_providers as dns_providers
from DNSAutocorrect.celery import app

from dynamicdns.models import MonitoredRecord, DNSService


@app.task
def run_dns_engine():
    """
    Performs the checks on all DNS records based on timing.
    :return:
    """

    # Pull DB Data
    records = MonitoredRecord.objects.all()
    services = DNSService.objects.all()

    # Extract record names
    record_names={}
    for record in records:
        record_names[record.name] = (record.dynamic_source_of_truth, record.source_of_truth)

    # Main loop
    for service in services:
        (get_records, update_record) = dns_providers.upa_resolver(service.provider)

        service_records = get_records(service.service_data)

        for record in service_records:
            print(f"Examining {record[0]}")

            # If this service record is a monitored record
            if record[0] in record_names.keys():
                print(f"Monitoring {record[0]}")

                # If source of truth is dynamic
                if record_names[record[0]][0]:
                    print(f"{record[0]} is Dynamic")
                    truth = get("https://api.ipify.org").text

                    if record[2] != truth:
                        print(f"{record[0]} MISMATCH: {record[2]} != {truth}")
                        new_record = record
                        new_record[2] = truth

                        if not update_record(service.service_data, record, new_record):
                            print(f"{record[0]} UPDATE FAILED")


                # If source of truth is static
                if record_names[record[0]][1]:
                    print(f"{record[0]} is Static")
                    truth = record_names[record[0]][1]
                    if record[2] != truth:
                        print(f"{record[0]} MISMATCH: {record[2]} != {truth}")
                        new_record = record
                        new_record[2] = truth

                        if not update_record(service.service_data, record, new_record):
                            print(f"{record[0]} UPDATE FAILED")

