# Created by gautamp at 09/06/25
Feature: Cart tests
  # Enter feature description here
  Scenario: 'Your cart is empty' message is shown for empty cart
     Given Open target main page
     When Click on Cart icon
     Then Verify 'Your cart is empty' message is shown
