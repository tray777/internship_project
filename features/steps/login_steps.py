from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given("Open Reelly main page")
def open_reelly_main_page(context):
    context.app.main_page.open_reelly_main_page()


@when("Type user email {email} into email textbox")
def user_email_textbox(context, email):
    context.app.main_page.user_email_textbox(email)


@when("Type incorrect user email {wrong_email} into email textbox")
def incorrect_user_email_textbox(context, wrong_email):
    context.app.main_page.incorrect_user_email_textbox(wrong_email)


@when("Type user password {password} into password textbox")
def user_password_textbox(context, password):
    context.app.main_page.user_password_textbox(password)


@when("Type incorrect user password {pass_word} into password textbox")
def incorrect_user_password_textbox(context, pass_word):
    context.app.main_page.incorrect_user_password_textbox(pass_word)


@when("Click Continue button")
def click_continue_button(context):
    context.app.main_page.click_continue_button()


@then("Verify message on screen {wrong_email_password} is displayed")
def verify_wrong_email_password(context, wrong_email_password):
    context.app.main_page.verify_wrong_email_password(wrong_email_password)


@when("Type uppercase characters {upper} of correct email address into email textbox")
def enter_uppercase_characters(context, upper):
    context.app.main_page.enter_uppercase_characters(upper)


@then("Verify user is on the login page")
def verify_user_is_on_login_page(context):
    context.app.main_page.verify_user_is_on_login_page()


#@then("Verify {wrong_email_password} message appears above the 'Continue' button")
    #context.app.main_page.verify_error_message_appears(wrong_email_password)