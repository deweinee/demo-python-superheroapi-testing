"""
HTTP client
"""

import requests

from settings import HEADERS, URL


class HttpClient:
    """
    HTTP client for superheroapi.com
    """

    def get_hero_list_page(self, path="/ids.html"):
        """
        Gets the page with a list of superheroes
        """
        response = requests.get(
            url=f'{URL}{path}',
            headers=HEADERS,
            timeout=3,
        )
        response.raise_for_status()
        return response
