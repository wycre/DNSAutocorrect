"""
Implements support for DNS APIs.
"""
from enum import Enum
from django.db import models

"""
MODIFY: Add imports for each DNS provider module
        Update the PROVIDER_MAPPINGS, Providers, and ProviderChoices definitions
"""
import moduleCloudflare.upa_functions as cloudflare

PROVIDER_MAPPINGS = {
    1: 'Cloudflare DNS',
}

class Providers(Enum):
    """
    Standard reference for available providers.
    """
    CLOUDFLARE = "1"

class ProviderChoices(models.TextChoices):
    CLOUDFLARE = "1", 'Cloudflare DNS',


def upa_resolver(provider_id):
    """
    Retrieves the UPA methods for a given DNS provider.
    :param provider_id: Providers enum value
    :return: Tuple containing (get_records, update_record) methods.
    """

    provider_id = int(provider_id)

    if provider_id not in PROVIDER_MAPPINGS.keys():
        raise ValueError('Invalid provider id')

    match provider_id:
        case 1:
            return (cloudflare.get_records, cloudflare.update_record)

        case _:
            raise ValueError('Invalid provider id')


if __name__ == '__main__':
    name = ""
    source_of_truth = "1.2.3.4"
    service_provider = Providers.CLOUDFLARE
    auth_token = ""
    str1 = ""

    get_method = cloudflare.get_records
    update_method = cloudflare.update_record

    get_method(str1, auth_token)
