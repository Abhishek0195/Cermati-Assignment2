# eBay Product Search Automation

This repository contains automated tests for the eBay website using pytest framework, WebdriverIO, and BDD (Behavior-Driven Development) approach.

## Approach

The automation script is written in Python using the pytest framework, which provides a simple and powerful way to write and execute tests. WebdriverIO is used as the WebDriver client library to interact with the web browser.

The test scenario described is implemented using the BDD approach, where the scenario steps are written in a human-readable format in the feature file using the Gherkin syntax. The test steps are then mapped to the corresponding Python functions using the pytest-bdd library.

The scenario "Access a Product via Search" performs the following steps:
1. Opens the eBay homepage.
2. Types the search string in the search bar.
3. Changes the search category and clicks the Search button.
4. Verifies that the page loads completely.
5. Verifies that the first result name matches the search string.

## Setup and Execution

To set up and run the code, follow these steps:

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies using pip:
pip install pytest pytest-bdd webdriverio

arduino
Copy code
3. Install the Selenium standalone server using npm:
npm install -g selenium-standalone

markdown
Copy code
4. Start the Selenium standalone server:
selenium-standalone start

sql
Copy code
5. Execute the tests using pytest:
pytest

vbnet
Copy code

Please make sure to replace the placeholder values in the feature file with actual search strings and categories you want to test.

## Folder Structure

The repository has the following structure:

test_search_product.py # Test script implementing the scenario
search_product.feature # Feature file containing the scenario steps
README.md # This file providing project information
markdown
Copy code

## Dependencies

The project has the following dependencies:

- Python 3.x
- pytest
- pytest-bdd
- WebdriverIO
- Selenium standalone server

Make sure to install these dependencies before running the tests.