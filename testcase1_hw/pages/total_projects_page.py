from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class TotalProjectsPage(Page):
    TOTAL_PROJECTS_TEXT = (By.XPATH, "//div[@class='page-title off_plan']")
    FILTERS_BUTTON = (By.XPATH, "//a[@class='filter-button w-inline-block']")
    HIGH_DEMAND_TAG = (By.XPATH, "//div[@class='_5-comission' and text()='High Demand']")

    def verify_text_displayed(self, total_projects_text):
        self.verify_text(total_projects_text, *self.TOTAL_PROJECTS_TEXT)

    def click_on_filters_button(self):
        sleep(5)
        self.wait_element_clickable_click(self.FILTERS_BUTTON)

    def verify_info_buttons(self, high_demand_tag):
        high_demand_tag = int(high_demand_tag)
        demand_tag = self.find_elements(*self.HIGH_DEMAND_TAG)
        assert len(demand_tag) == high_demand_tag, f'Expected {high_demand_tag} links, but got {len(demand_tag)}'
