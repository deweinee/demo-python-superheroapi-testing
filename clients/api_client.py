"""
API client
"""

import requests

from settings import HEADERS, URL


class ApiClient:
    """
    API client for superheroapi.com
    """

    def get_by_id(self, params, path="/api/336778981550281/{superheroId}"):
        """
        Gets superhero info by superhero id
        """
        path = path.format(**params)
        response = requests.get(
            url=f'{URL}{path}',
            headers=HEADERS,
            timeout=3,
        )
        response.raise_for_status()
        return response
