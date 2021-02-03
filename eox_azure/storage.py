"""
Module that defines the AzureStorage Wrapper.
"""
from storages.backends.azure_storage import AzureStorage


class AzureStorageExtended(AzureStorage):  # pylint: disable=abstract-method
    """
    A wrapper around the django-stores implementation for Azure blob storage
    so that it is fully comptaible. The version in the library's repository
    is out of date
    """

    def __init__(self, container=None, expiration_secs=None, *args, **kwargs):  # pylint: disable=keyword-arg-before-vararg, unused-argument
        """
        Override base implementation so that we can accept a container
        parameter and an expiration on urls
        """

        super(AzureStorageExtended, self).__init__()

        self.expiration_secs = expiration_secs

        if container:
            self.azure_container = container
