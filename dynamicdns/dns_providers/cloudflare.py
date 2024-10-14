"""
Cloudflare DNS
"""
from requests import get, post, patch
import json, datetime


def get_records(str1, auth_key):
    """
    Obtains a list of records from the DNS Provider
    :param str1: Cloudflare Zone ID
    :param auth_key:
    :return: List of records retrieved, or False if an error occurs
    """

    # Build request parameters
    headers = {
        'Authorization': 'Bearer ' + auth_key,
        'Content-Type': 'application/json'
    }
    url = 'https://api.cloudflare.com/client/v4/zones/' + str1 + '/dns_records'

    # Make Request
    response = json.loads(get(url, headers=headers).text)

    # TODO add error handling in here

    # Data parsing and reorg
    data = []
    for record in response['result']:
        data.append({
            'name': record['name'],
            'type': record['type'],
            'data': record['content'],
            'id': record['id'],
        })

    return data


def update_record(url, auth_key):
    """
    Updates a record with the DNS Provider
    :param url: API
    :param auth_key:
    :return:
    """
    pass
