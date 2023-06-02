# search_product.feature

Feature: Access a Product via Search

  Scenario: Access a Product via Search
    Given I am on the eBay homepage
    When I type '<search_string>' in the search bar
    And I change the Search category to '<category>' and click Search
    Then the page loads completely
    And the first result name matches with the search string
