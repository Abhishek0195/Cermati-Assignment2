# test_search_product.py

import pytest
from webdriverio import remote
from pytest_bdd import given, when, then, scenario


# Set up WebdriverIO configuration
config = {
    'hostname': 'localhost',
    'port': 4444,
    'capabilities': [{
        'browserName': 'chrome'
    }]
}

# Create a WebdriverIO session
driver = remote(config)


# Scenario: Access a Product via Search
@scenario('search_product.feature', 'Access a Product via Search')
def test_search_product():
    pass


@given("I am on the eBay homepage")
def i_am_on_ebay_homepage():
    driver.url('https://www.ebay.com')


@when("I type '<search_string>' in the search bar")
def i_type_search_string_in_search_bar(search_string):
    search_input = driver.find_element('#gh-ac')
    search_input.clear()
    search_input.send_keys(search_string)


@when("I change the Search category to '<category>' and click Search")
def i_change_search_category_and_click_search(category):
    category_dropdown = driver.find_element('#gh-cat')
    category_dropdown.select_by_visible_text(category)
    search_button = driver.find_element('#gh-btn')
    search_button.click()


@then("the page loads completely")
def page_loads_completely():
    driver.wait_until(lambda s: s.execute_script('return document.readyState') == 'complete', timeout=10)


@then("the first result name matches with the search string")
def first_result_name_matches_search_string():
    first_result = driver.find_element('.srp-results li:first-child .s-item__title')
    search_string = driver.execute_script('return arguments[0].innerText;', first_result)
    assert search_string == pytest.current_scenario.search_string


# Execute the test scenario
test_search_product()
