import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect
from pages.home_page import HomePage

scenarios('../features/basic_search.feature')

@pytest.fixture
def home_page(page):
    return HomePage(page)

@given("As an not logged user navigate to homepage https://www.kiwi.com/en/")
def navigate_home(home_page):
    home_page.navigate()

@when("I select one-way trip type")
def select_one_way(home_page):
    home_page.select_one_way()

@when("Set as departure airport RTM")
def set_departure(home_page):
    home_page.set_departure_rtm()

@when("Set the arrival Airport MAD")
def set_arrival(home_page):
    home_page.set_arrival_mad()

@when("Set the departure time 1 week in the future starting current date")
def set_future_date(home_page):
    home_page.set_future_date()

@when("Uncheck the `Check accommodation with booking.com` option")
def uncheck_accommodation(home_page):
    home_page.uncheck_accommodation()

@when("Click the search button")
def click_search(home_page):
    home_page.search()

@then("I am redirected to search results page")
def verify_results(home_page):
    expect(home_page.page.locator("[data-test=\"ResultCardWrapper\"]").first).to_be_visible()