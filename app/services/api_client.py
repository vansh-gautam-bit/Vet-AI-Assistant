import httpx
from app.config import settings

class APIClient:
    def __init__(self):
        self.base_url = settings.BACKEND_URL
        self.token = None

        self.client = httpx.Client(
            base_url=self.base_url,
            timeout=30.0,
        )