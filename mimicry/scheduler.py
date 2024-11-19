
from dataclasses import asdict, dataclass
from typing import Dict, Optional

MAX_DELAY = 120
MOCKS_POOL = {}

@dataclass
class Mock:
    path: str
    headers: Optional[Dict[str, str]] = None
    status_code: int = 200    
    body: str = ''
    delay: int = 0

    def __post_init__(self):
        if not isinstance(self.path, str) or not self.path.startswith('/'):
            raise ValueError(f"Path must be a string starting with '/'. You sent: '{self.path}'")
        if self.delay > MAX_DELAY:
            raise ValueError(f"Delay must be less than {MAX_DELAY}. You sent: '{self.delay}'")


class MockScheduler:
    def __init__(self):
        self.mocks = {}

    def create_mock(self, mock_data: dict):
        """
        Schedule a mock for a specific endpoint.
        :param path: The endpoint path.
        :param status: HTTP status code.
        :param headers: Optional HTTP headers as a dictionary.
        :param body: The response body.
        :param delay: Optional delay before responding, in seconds.
        """
        mock_data = asdict(mock_data)
        path = mock_data.pop('path')
        MOCKS_POOL[path] = mock_data
        print(path)
        print(mock_data)

    def update_mock(self, mock_data: dict):
        """
        Update an existing mock for a specific endpoint.
        :param path: The endpoint path.
        :param status: HTTP status code.
        :param headers: Optional HTTP headers as a dictionary.
        :param body: The response body.
        :param delay: Optional delay before responding, in seconds.
        """
        mock_data = asdict(mock_data)
        path = mock_data.pop('path')
        MOCKS_POOL[path] = mock_data
        print(path)
        print(mock_data)

    def clear_mocks(self):
        MOCKS_POOL.clear()

    def get_mock(self, path: str):
        """Retrieve the mock for a specific endpoint."""
        return MOCKS_POOL.get(path, None)
   
