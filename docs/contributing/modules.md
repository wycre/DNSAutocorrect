# Writing a new DNS provider module

Make a new file in [`/dynamicdns_dns_providers`](..%2F..%2Fdynamicdns%2Fdns_providers) with the following template:
```python
"""
Template for provider modules
"""
def get_records(str1, str2, auth_key):
    """
    Obtains a list of records from the DNS Provider
    :param str1: CHANGETHIS, optional, by convention, the larger structure that contains dns records (i.e. Cloudflare zones)
    :param str2: CHANGETHIS, optional, additional information required to make the request
    :param auth_key:
    :return:
    """
    # Build request parameters (i.e. header, url, etc.)
    
    # Make request
    
    # Error Handling
    
    # Data Parsing & Cleanup
    """
    Data should take the form of a list of dicts
    Each dict should have _at least_ the following keys:
    - name
    - type
    - data
    - id (API reference to record ID)
    """
    
    # Return
    pass


def update_record(url, auth_key):
    """
    Updates a record with the DNS Provider
    :param url: API
    :param auth_key:
    :return:
    """
    pass

```

Records should be returned from 
