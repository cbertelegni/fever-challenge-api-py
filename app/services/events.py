# import xml.etree.ElementTree as ET
from app.clients.provider import ProviderClient


class EventService:
    def __init__(self, provider_client: ProviderClient) -> None:
        self.provider_client = provider_client

    @classmethod
    def create(cls):
        provider_client = ProviderClient.create()
        return cls(provider_client=provider_client)

    def update_events_from_provider(self):
        pass
