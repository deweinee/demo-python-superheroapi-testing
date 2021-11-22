import requests

from settings import HEADERS, URL


class ApiClient:

    def get_by_id(self, params, path="/api/336778981550281/{superheroId}"):
        """

        Gets superhero info by superhero id
        """
        path = path.format(**params)
        response = requests.get(
            url=f'{URL}{path}',
            headers=HEADERS,
        )
        response.raise_for_status()
        return response
