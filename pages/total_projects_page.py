from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class TotalProjectsPage(Page):
    TOTAL_PROJECTS_TEXT = (By.XPATH, "//div[@class='page-title off_plan']")
    FILTERS_BUTTON = (By.XPATH, "//a[@class='filter-button w-inline-block']")
    HIGH_DEMAND_TAG = (By.XPATH, "//div[@class='_5-comission' and text()='High Demand']")
    ALL_PRODUCTS = (By.XPATH, "//a[@wized='cardOfProperty']")
    CLICK_NEXT_PAGE = (By.XPATH, "//a[@wized='nextPageProperties']")

    def verify_text_displayed(self, total_projects_text):
        self.wait_element_visible(*self.TOTAL_PROJECTS_TEXT)
        assert self.find_element(*self.TOTAL_PROJECTS_TEXT).is_displayed()
        #self.verify_text(total_projects_text, *self.TOTAL_PROJECTS_TEXT)

    def click_on_filters_button(self):
        sleep(5)
        self.wait_element_clickable_click(self.FILTERS_BUTTON)

    def verify_high_demand_tag(self):
        count = 1
        while count < 13:
            self.driver.execute_script("window.scrollBy(0,2000)", "")
            sleep(1)
            self.driver.execute_script("window.scrollBy(0,2000)", "")

            all_products = self.find_elements(*self.ALL_PRODUCTS)

            for product in all_products:
                self.wait_element_visible(*self.HIGH_DEMAND_TAG)
                title = product.find_element(*self.HIGH_DEMAND_TAG).text

                assert title, 'product title not shown'

            self.wait_element_clickable(*self.CLICK_NEXT_PAGE)
            self.find_element(*self.CLICK_NEXT_PAGE).click()

            count += 1


