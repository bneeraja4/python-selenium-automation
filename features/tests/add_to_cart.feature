Feature: add a product to cart

    Scenario: User can add a product to cart
    Given Open target main page
    When Search for soap
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart should contain at least one item

