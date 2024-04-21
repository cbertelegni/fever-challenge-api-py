from app.core.config import settings
from app.clients.base import BaseClient


class ProviderClient(BaseClient):
    @classmethod
    def create(cls, base_url=settings.PROVIDER_BASE_URL):
        return cls(base_url=base_url)

    def fetch_xml_events(self):
        method = "api/events"
        response = self.get(method)
        response.raise_for_status()
        return response.content
