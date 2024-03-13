from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SideMenuOffPlan(Page):

    OFF_PLAN_BUTTON = (By.XPATH, "//div[@class='menu-button-text' and text()='Off-plan']")

    def click_off_plan_icon(self):
        self.wait_element_clickable_click(self.OFF_PLAN_BUTTON)