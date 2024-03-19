from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MoreFiltersPage(Page):
    HIGH_DEMAND_BUTTON = (By.XPATH, "//div[text()='High Demand' and @class='tag-text-proparties']")

    def click_on_high_demand_button(self):
        sleep(6)
        self.find_element(*self.HIGH_DEMAND_BUTTON).click()
        sleep(6)
