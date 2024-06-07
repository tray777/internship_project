# Created by Tracy Arispe at 5/29/2024
Feature: Test Scenarios for login functionality

  @TestID_1
  Scenario: User can login to account with proper credentials
    Given Open Reelly main page
    Then Verify user is on the login page
    When Type user email arispe.tracy@gmail.com into email textbox
    When Type user password abc123 into password textbox
    When Click Continue button
    Then Verify that Total projects text is displayed

  @TestID_2
  Scenario: user gets error message logging in with wrong password
    Given Open Reelly main page
    Then Verify user is on the login page
    When Type incorrect user email arispe.tracy@gmail.com into email textbox
    When Type incorrect user password abcabc into password textbox
    When Click Continue button
    Then Verify message on screen Wrong email address or password. is displayed

    @TestID_3 @Bug
  Scenario: User gets error message logging in with username but no password
    Given Open Reelly main page
    Then Verify user is on the login page
    When Type user email arispe.tracy@gmail.com into email textbox
    When Click Continue button
    Then Verify message on screen Wrong email address or password. is displayed

   @TestID_5 @bug
  Scenario: User gets error message logging in with wrong email and password
    Given Open Reelly main page
    Then Verify user is on the login page
    When Type incorrect user email tracy@gmail.com into email textbox
    When Type incorrect user password abcabc into password textbox
    When Click Continue button
    Then Verify message on screen Wrong email address or password. is displayed


  @TestID_6 @bug
  Scenario: No error message logging in with uppercase characters for lower case email while using correct password
    Given Open Reelly main page
    Then Verify user is on the login page
    When Type uppercase characters ARISPE.TRACY@gmail.com of correct email address into email textbox
    When Type user password abc123 into password textbox
    When Click Continue button
    Then Verify that Total projects text is displayed


  @TestID_7 @bug
  Scenario: User gets error message logging in with all uppercase email but incorrect password
    Given Open Reelly main page
    Then Verify user is on the login page
    When Type uppercase characters ARISPE.TRACY@gmail.com of correct email address into email textbox
    When Type incorrect user password abcabc into password textbox
    When Click Continue button
    Then Verify message on screen Wrong email address or password. is displayed

  @TestID_8
  Scenario: User gets error message logging in with correct email but missing @ character using correct password
    Given Open Reelly main page
    Then Verify user is on the login page
    When Type user email arispe.tracygmail.com into email textbox
    When Type user password abc123 into password textbox
    When Click Continue button
    Then Verify message on screen Wrong email address or password. is displayed

  @TestID_9 @bug
  Scenario: User gets error message logging in with correct email but missing .com in email
    Given Open Reelly main page
    Then Verify user is on the login page
    When Type user email arispe.tracy@gmail into email textbox
    When Type user password abc123 into password textbox
    When Click Continue button
    Then Verify message on screen Wrong email address or password. is displayed

  @TestID_10 @bug
  Scenario: User gets error message inputting multiple numbers instead of email in email text box using correct password
    Given Open Reelly main page
    Then Verify user is on the login page
    When Type user email 8675309 into email textbox
    When Type user password abc123 into password textbox
    When Click Continue button
    Then Verify message on screen Wrong email address or password. is displayed

  @TestID_4
  Scenario: Error message appears above the 'Continue' button logging in with incorrect password
    Given Open Reelly main page
    Then Verify user is on the login page
    When Type user email arispe.tracy@gmail into email textbox
    When Type incorrect user password abcabc into password textbox
    When Click Continue button
    Then Verify 'Wrong email address or password' message appears above the 'Continue' button


