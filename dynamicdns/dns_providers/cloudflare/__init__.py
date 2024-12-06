"""
Cloudflare DNS
"""
from requests import get, post, patch
import json, datetime

def get_records(service_data):
    """
    UPA method to get records from the DNS Provider
    :param service_data: JSON string holding data specific to the DNS provider
    :return: List of Records
    """
    s_data = json.loads(service_data)
    headers = {
        'Authorization': 'Bearer ' + s_data['auth_token'],
        'Content-Type': 'application/json'
    }
    url = 'https://api.cloudflare.com/client/v4/zones/' + s_data['zone_id'] + '/dns_records'

    # Make request
    response = json.loads(get(url, headers=headers).text)

    # TODO add error handling here

    # Data parsing and reorg
    data = []
    for record in response['result']:
        data.append([
            record['name'],
            record['type'],
            record['content'],
            record['id']
        ])

    return data


def update_record(service_data, original_record, updated_record):
    """
    UPA method to update a record in the DNS Provider
    :param service_data: JSON string holding data specific to the DNS provider
    :param original_record: The record that needs to be updated
    :param updated_record: The expected record state after updating
    :return: Boolean indicating success or failure
    """
    # Assemble Request Data
    s_data = json.loads(service_data)
    headers = {
        'Authorization': 'Bearer ' + s_data['auth_token'],
        'Content-Type': 'application/json'
    }
    url = 'https://api.cloudflare.com/client/v4/zones/' + s_data['zone_id'] + '/dns_records/' + original_record[3]

    # Build payload
    data = {
        'content': updated_record[2],
        'name': updated_record[0],
        'type': updated_record[1],
        'id': updated_record[3]
    }

    # Make request
    response = json.loads(patch(url, headers=headers, json=data).text)

    if response['success'] is True:
        return True
    else:
        print('==Record Update Failed==')
        print(response)
        return False



if __name__ == '__main__':
    """Test function"""
    zone_id = '"zone_id"'
    api_key = '"api_key"'
    test_service_data = '{{"provider_name":"Cloudflare","auth_token":{},"zone_id":{}}}'.format(api_key, zone_id)

    all_records = get_records(test_service_data)
    print(all_records)

    dummy1 = all_records[4]
    new_dummy = (dummy1[0], dummy1[1], '1.2.3.4', dummy1[3])
    status = update_record(test_service_data, dummy1, new_dummy)
    print(status)



