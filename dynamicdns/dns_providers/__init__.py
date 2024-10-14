"""
Implements support for DNS APIs.
"""
from enum import Enum
import cloudflare


class Providers(Enum):
    """
    Standard reference for available providers.
    """
    CLOUDFLARE = 1


PROVIDER_MAPPINGS = {
    Providers.CLOUDFLARE: 'Cloudflare DNS',
}

if __name__ == '__main__':
    name = ""
    source_of_truth = "1.2.3.4"
    service_provider = Providers.CLOUDFLARE
    auth_token = ""
    str1 = ""

    get_method = cloudflare.get_records
    update_method = cloudflare.update_record

    get_method(str1, auth_token)
