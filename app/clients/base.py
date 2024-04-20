import requests
from requests import Response
from urllib.parse import urljoin


class BaseClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def get_url(self, method: str) -> str:
        return urljoin(self.base_url, method)

    def get(self, method: str) -> Response:
        url = self.get_url(method)
        response = requests.get(url)
        return response
