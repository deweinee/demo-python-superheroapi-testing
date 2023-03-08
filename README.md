# API autotests example for [superheroapi.com](https://www.superheroapi.com)

### Technology stack:
Python, PyTest, PyHamcrest, Requests, allure-pytest

### Tests
1. Superhero with "woman" in name indeed has "gender": "female"
- Get page content https://www.superheroapi.com/ids.html
- Detect characters that have "woman" in their name (case insensitive)
- For all detected characters, check if the information about them indicates appearance/gender "Female"
