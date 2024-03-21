from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(Page):
    CONTINUE_BUTTON = (By.XPATH, "//a[@wized='loginButton']")
    EMAIL_TEXT = (By.XPATH, "//input[@id='email-2']")
    PASSWORD_TEXT = (By.XPATH, "//input[@id='field']")

    def open_reelly_main_page(self):
        self.open('https://soft.reelly.io/sign-in')

    def user_email_textbox(self, email):
        self.input_text(email, *self.EMAIL_TEXT)

    def user_password_textbox(self, password):
        self.input_text(password, *self.PASSWORD_TEXT)

    def click_on_cart_icon(self):
        self.wait_element_clickable_click(self.CONTINUE_BUTTON)


