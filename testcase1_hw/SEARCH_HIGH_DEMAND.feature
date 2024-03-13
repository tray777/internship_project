Feature: Test Scenarios for search filter functionality

  Scenario: User can filter by sale status High Demand
    Given Open Reelly main page
    When Type user email arispe.tracy@gmail.com into email textbox
    When Type user password abc123 into password textbox
    When Click Continue button
    When Click on off plan icon at the left side menu
    Then Verify that Total projects text is displayed
    When Click on Filters button
    When Click on High Demand button
    Then Verify 24 products on the page contain the High Demand tag
