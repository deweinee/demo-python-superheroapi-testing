# API autotests example for [superheroapi.com](https://www.superheroapi.com)

### Technology stack
**Python, PyTest, PyHamcrest, Requests, allure-pytest**

### Tests
1. Superhero with "woman" in name indeed has "gender": "female"
   - Get page content https://www.superheroapi.com/ids.html
   - Detect characters that have "woman" in their name (case insensitive)
   - For all detected characters, check if the information about them indicates appearance/gender "Female"

-----

#### Very basic CI/CD is set up for this repository:
  - A workflow with pylint checks is created in GitHub Actions
  - Direct merging into main is prohibited, all commits must be made to a non-protected branch and submitted via a pull request
  - All conversations on code must be resolved before a pull request can be merged
  - Pylint checks must pass before merging a pull request
  