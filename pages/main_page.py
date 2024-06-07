from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(Page):
    CONTINUE_BUTTON = (By.XPATH, "//a[@wized='loginButton']")
    EMAIL_TEXT = (By.XPATH, "//input[@id='email-2']")
    PASSWORD_TEXT = (By.XPATH, "//input[@id='field']")
    ERROR_MESSAGE2 =(By.XPATH, "//div[text()='Wrong email address or password.']")
    ERROR_MESSAGE =(By.XPATH, "//div[@wized='errorMessageLogin']")
    VERIFY_LOGIN = (By.XPATH, "//h1[text()='Sign in or create new account']")

    def open_reelly_main_page(self):
        self.open('https://soft.reelly.io/sign-in')

    def user_email_textbox(self, email):
        self.input_text(email, *self.EMAIL_TEXT)

    def enter_uppercase_characters(self, upper):
        self.input_text(upper, *self.EMAIL_TEXT)

    def incorrect_user_email_textbox(self, wrong_email):
        self.input_text(wrong_email, *self.EMAIL_TEXT)

    def user_password_textbox(self, password):
        self.input_text(password, *self.PASSWORD_TEXT)

    def incorrect_user_password_textbox(self, pass_word):
        self.input_text(pass_word, *self.PASSWORD_TEXT)

    def click_continue_button(self):
        self.wait_element_clickable_click(self.CONTINUE_BUTTON)
        #sleep(6)

    def verify_wrong_email_password(self, wrong_email_password):
        self.wait_element_visible(*self.ERROR_MESSAGE)
        actual_email = self.find_element(*self.ERROR_MESSAGE).text
        print('result ' + actual_email)
        assert wrong_email_password == actual_email, f"Expected '{wrong_email_password}', but got '{actual_email}'"

    def verify_user_is_on_login_page(self):
        verify_page = self.find_element(*self.VERIFY_LOGIN).text
        assert verify_page

    def verify_error_message_appears(self, wrong_email_password):
        pass





