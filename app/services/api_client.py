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

    def login(self):
        """
        Authenticate with the backend and store the JWT token.
        """      

        response = self.client.post(
            "/auth/login",
            data={
                "username": settings.EMAIL,
                "password": settings.PASSWORD,
            },
        )

        response.raise_for_status()

        self.token = response.json()["access_token"]

    @property
    def headers(self):
        """
        Return authorization headers.
        Automatically logs in if no token is available.
        """

        if self.token is None:
            self.login()

            return {
                "Authorization": f"Bearer {self.token}"
            }
    def get(self, endpoint: str, params: dict | None = None):
        response = self.client.get(
            endpoint,
            params=params,
            headers = self.headers,
        )    

        response.raise_for_status()

        return response.json()

    def post(self, endpoint: str, json: dict):
        response = self.client.post(
            endpoint,
            json=json,
            headers=self.headers,
        )

        response.raise_for_status()

        return response.json()

    def put(self, endpoint: str, json: dict):
        response = self.client.put(
            endpoint,
            json=json,
            headers=self.headers,
        )
        response.raise_for_status()

        return response.json()

    def delete(self, endpoint: str):
        response = self.client.delete(
            endpoint,
            headers=self.headers,
        )

        response.raise_for_status()

        return response.json()

    def close(self):
        self.client.close()

api_client =  APIClient()        