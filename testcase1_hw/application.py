from pages.main_page import MainPage
from pages.more_filters_page import MoreFiltersPage
from pages.base_page import Page
from pages.side_menu_off_plan import SideMenuOffPlan
from pages.total_projects_page import TotalProjectsPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.more_filters_page = MoreFiltersPage(driver)
        self.page = Page(driver)
        self.side_menu_off_plan = SideMenuOffPlan(driver)
        self.total_projects_page = TotalProjectsPage(driver)