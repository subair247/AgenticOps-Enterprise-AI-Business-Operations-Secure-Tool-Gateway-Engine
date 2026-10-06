import requests

class APIClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.headers = {
            "X-API-Key": api_key,
            "Content-Type": "application/json"
        }

    def run_agent(self, goal: str, role: str = "standard_agent") -> requests.Response:
        """Sends POST request to FastAPI backend to run agent loop."""
        url = f"{self.base_url}/run"
        payload = {"goal": goal, "role": role}
        try:
            response = requests.post(url, json=payload, headers=self.headers, timeout=30)
            return response
        except Exception as e:
            raise Exception(f"API Connection Error: {str(e)}")