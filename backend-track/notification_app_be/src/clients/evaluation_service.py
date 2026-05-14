import json
from urllib.request import Request, urlopen


class EvaluationServiceClient:
    """Small standard-library client for the evaluation notification API."""

    base_url = "http://4.224.186.213/evaluation-service"

    def __init__(self, access_token: str):
        self.access_token = access_token

    def get_notifications(self) -> list[dict]:
        request = Request(
            f"{self.base_url}/notifications",
            headers={"Authorization": f"Bearer {self.access_token}"},
            method="GET",
        )
        with urlopen(request, timeout=15) as response:
            payload = json.loads(response.read().decode("utf-8"))
        return payload["notifications"]
