"""
MODIFY: Implement UPA functions here, then update the dns_providers module to access them
"""

from requests import get, post, patch
import json, datetime

def get_records(service_data):
    """
    UPA method to get records from the DNS Provider
    :param service_data: JSON string holding data specific to the DNS provider
    :return: List of Records
    """
    pass

def update_record(service_data, original_record, updated_record):
    """
    UPA method to update a record in the DNS Provider
    :param service_data: JSON string holding data specific to the DNS provider
    :param original_record: The record that needs to be updated
    :param updated_record: The expected record state after updating
    :return: Boolean indicating success or failure
    """
    pass
