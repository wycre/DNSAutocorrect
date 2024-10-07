"""
This file holds the interface for provider modules. Implement this interface in a new file to add new provider support.
"""
from abc import ABC, abstractmethod


class Provider(ABC):
    @abstractmethod
    def get_records(self, url, auth_key):
        """
        Obtains a list of records from the DNS Provider
        :param url: API Request URL
        :param auth_key:
        :return:
        """
        pass

    @abstractmethod
    def update_record(self, url, auth_key):
        pass
