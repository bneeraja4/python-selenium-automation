# Created by gautamp at 09/06/25
Feature: Verify Sign In form opened
  Scenario: Verify Sign In form opened
    Given Open target main page
     When Click Account
     Then From right side navigation menu, click Sign In
     Then Verify Sign In form opened