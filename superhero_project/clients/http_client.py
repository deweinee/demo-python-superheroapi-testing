import requests

from superhero_project.settings import HEADERS, URL


class HttpClient:

    def get_hero_list_page(self, path="/ids.html"):
        """

        Gets the page with a list of superheroes
        """
        response = requests.get(
            url=f'{URL}{path}',
            headers=HEADERS,
        )
        response.raise_for_status()
        return response
