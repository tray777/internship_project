from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when("Click on off plan icon at the left side menu")
def click_off_plan_icon(context):
    context.app.side_menu_off_plan.click_off_plan_icon()


@then("Verify that {total_projects_text} text is displayed")
def verify_text_displayed(context, total_projects_text):
    context.app.total_projects_page.verify_text_displayed(total_projects_text)


@when("Click on Filters button")
def click_on_filters_button(context):
    context.app.total_projects_page.click_on_filters_button()


@when("Click on High Demand button")
def click_on_high_demand_button(context):
    context.app.more_filters_page.click_on_high_demand_button()


@then("Verify all products contain the High Demand tag")
def verify_high_demand_tag(context):
    context.app.total_projects_page.verify_high_demand_tag()