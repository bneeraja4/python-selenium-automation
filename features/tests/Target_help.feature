Feature: Target help page UI
  Scenario Outline:Verify UI elements are present on the Target help page
    Given open Target help page
    Then verify <UI element>
    Examples:
    |UI element                             |
    |Target Help header                     |
    |search help input field                |
    |search button                          |
    |What would you like to do section      |
    |Browse all help pages text is displayed|

