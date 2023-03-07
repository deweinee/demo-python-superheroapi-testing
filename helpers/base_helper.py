"""
Helpers
"""

import re

from clients.http_client import HttpClient


def superhero_id_with_woman_in_name() -> list:
    """
    Gets a list of superheroes with "woman" in their names
    Output: list of ids
    """
    response = HttpClient().get_hero_list_page()
    superhero_id = re.findall(r'<tr><td>(.*?)</td><td>', re.sub("\n", "", re.sub(" +", "", response.text)))
    superhero_name = re.findall(r'</td><td>(.*?)</td></tr>', re.sub("\n", "", re.sub(" +", "", response.text)))
    superhero_whole_list = dict(zip(superhero_id, superhero_name))
    superhero_woman = {k: v for k, v in superhero_whole_list.items() if re.match(r".*woman.*", ''.join(v).lower())}
    return list(superhero_woman.keys())
