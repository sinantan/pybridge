import requests
from typing import Dict, Any, Optional, Union


class PyBridge:
    def __init__(self, base_url: str, headers: Optional[Dict[str, Union[str, int]]] = None):
        self.base_url = base_url
        self.headers = headers
        self._schema = self._fetch_schema()

    def _fetch_schema(self) -> Dict[str, Any]:
        """Retrieve the OpenAPI schema from the base URL."""
        try:
            response = requests.get(f"{self.base_url}/openapi.json")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch schema: {e}")

    def _build_request(self, path: str, method: str, params: Dict[str, Any]):
        """Construct and send an API request."""
        endpoint = f"{self.base_url}/{path}"
        try:
            response = requests.request(method, endpoint, params=params, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")

    def _create_method(self, path: str, method: str):
        """Create a method for the given path and HTTP method."""
        def request_func(**params):
            return self._build_request(path, method, params)

        return request_func

    def __getattr__(self, name: str):
        """Dynamically create methods for API endpoints based on the schema."""
        for path, methods in self._schema["paths"].items():
            method_name = path.strip('/').replace('-', '_').replace('/', '_')
            if name.startswith(method_name):
                method = list(methods.keys())[0]
                return self._create_method(path, method)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
