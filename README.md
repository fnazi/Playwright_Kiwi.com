# Kiwi.com Flight Search Automation
```txt
@basic_search
Feature: Basic search form
    Scenario: T1 - One way flight search
        Given As an not logged user navigate to homepage https://www.kiwi.com/en/
        When I select one-way trip type
        And Set as departure airport RTM
        And Set the arrival Airport MAD
        And Set the departure time 1 week in the future starting current date
        And Uncheck the `Check accommodation with booking.com` option
        And Click the search button
        Then I am redirected to search results page
```

## Project Overview
This test automation framework validates the basic flight search functionality on Kiwi.com using:
- **Python** + **Playwright** for browser automation
- **pytest** + **pytest-bdd** for test execution
- **Page Object Model** for maintainability
- **Docker** for containerized execution
- **GitHub Actions** for CI/CD

## Project Structure
```bash
Kiwi.com_Py_Playwright/
├── features/
│   └── basic_search.feature    # Gherkin test scenarios
├── pages/
│   └── home_page.py            # Page Object Model
├── tests/
│   └── test_basic_search.py    # Step implementations
├── conftest.py                 # Pytest fixtures
├── pytest.ini                  # Test configuration
└── requirements.txt            # Dependency list
```

## 1. Dependancies

requirements.txt
```txt
playwright==1.42.0          # Browser automation
pytest==7.4.4               # Test framework
pytest-bdd==6.1.1           # BDD implementation
pytest-playwright==0.4.0     # Playwright integration
pytest-html==4.1.1           # HTML reporting
pytest-rerunfailures==12.0   # Test retries
python-dateutil==2.9.0.post0 # Date handling
```

To install:
```bash
pip install -r requirements.txt
playwright install
```

## 2. Running Specific Test from 100+ Suite
Below methods can be used for running specific test cases

By marker tag:
```bash
pytest -m basic_search
```
By scenario name:
```bash
pytest -k "One_way_flight_search"
```
By file:
```bash
pytest tests/test_basic_search.py
```
Running all tests:
```bash
pytest 
```

<!-- To run in headed mode
Change headless=False in conftest.py and run using the above methods -->

## 2. View HTML report
```bash
open results/report.html  # macOS
```
## 3.  Docker Setup
Create dockerfile
````bash
# Build image
docker build -t kiwi-tests .

# Run tests
docker run -it --rm kiwi-tests
````
## 4.  CI/CD Setup (GitHub Actions)
```txt
CI Configuration (.github/workflows/tests.yml)

GitHub Actions Flow
1.Push code to GitHub
2.Actions automatically runs tests
3.View results in GitHub's "Actions" tab
4.Download report from Artifacts
```