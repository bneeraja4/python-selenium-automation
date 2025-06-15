Feature: Tests for Target Search

  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify search worked for tea