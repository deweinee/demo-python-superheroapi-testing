import allure
import pytest
from hamcrest import assert_that, equal_to

from clients.api_client import ApiClient
from helpers.base_helper import superhero_id_with_woman_in_name


@allure.title('Superhero with "woman" in name indeed has "gender": "female"')
@pytest.mark.parametrize('superhero_id', [item for id_list in [superhero_id_with_woman_in_name()] for item in id_list])
def test_superhero_is_woman(superhero_id):
    data = {
        'superheroId': superhero_id
    }
    superhero_woman_in_name = ApiClient().get_by_id(params=data).json()
    assert_that(superhero_woman_in_name['appearance']['gender'].lower(),
                equal_to("female"),
                reason=f'{superhero_woman_in_name["name"]} is in fact {superhero_woman_in_name["appearance"]["gender"]}')
