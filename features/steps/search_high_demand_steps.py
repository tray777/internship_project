from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

HIGH_DEMAND_TAG = (By.XPATH, "//div[@class='_5-comission' and text()='High Demand']")
ALL_PRODUCTS = (By.XPATH, "//a[@wized='cardOfProperty']")
# CLICK_NEXT_PAGE = (By.XPATH, "//a[@class='pagination__button w-inline-block']")
CLICK_NEXT_PAGE = (By.XPATH, "//a[@wized='nextPageProperties']")


@given("Open Reelly main page")
def open_reelly_main_page(context):
    # context.driver.get('https://soft.reelly.io/sign-in')
    context.app.main_page.open_reelly_main_page()


@when("Type user email {email} into email textbox")
def user_email_textbox(context, email):
    # context.driver.find_element(*EMAIL_TEXT).send_keys(email)
    # sleep(6) #leave in
    context.app.main_page.user_email_textbox(email)


@when("Type user password {password} into password textbox")
def user_password_textbox(context, password):
    # context.driver.find_element(*PASSWORD_TEXT).send_keys(password)
    # sleep(6) #leave in
    context.app.main_page.user_password_textbox(password)


@when("Click Continue button")
def click_on_cart_icon(context):
    # context.driver.find_element(*CONTINUE_BUTTON).click()
    # sleep(6)
    context.app.main_page.click_on_cart_icon()


@when("Click on off plan icon at the left side menu")
def click_off_plan_icon(context):
    # context.driver.find_element(*OFF_PLAN_BUTTON).click()
    # sleep(6)
    context.app.side_menu_off_plan.click_off_plan_icon()


@then("Verify that {total_projects_text} text is displayed")
def verify_text_displayed(context, total_projects_text):
    # context.wait.until(EC.presence_of_element_located(TOTAL_PROJECTS_TEXT), message='Message not shown')
    # actual_text = context.driver.find_element(*TOTAL_PROJECTS_TEXT).text
    # assert total_projects_text == actual_text, f'Expected message {total_projects_text} not in {actual_text}'
    context.app.total_projects_page.verify_text_displayed(total_projects_text)


@when("Click on Filters button")
def click_on_filters_button(context):
    # context.driver.find_element(*FILTERS_BUTTON).click()
    # sleep(6)
    context.app.total_projects_page.click_on_filters_button()


@when("Click on High Demand button")
def click_on_high_demand_button(context):
    # context.driver.find_element(*HIGH_DEMAND_BUTTON).click()
    # sleep(10)
    context.app.more_filters_page.click_on_high_demand_button()


'''@then("Verify {high_demand_tag} products on the page contain the High Demand tag")
def verify_info_buttons(context, high_demand_tag):
    # high_demand_tag = int(high_demand_tag)
    # demand_tag = context.driver.find_elements(*HIGH_DEMAND_TAG)
    # assert len(demand_tag) == high_demand_tag, f'Expected {high_demand_tag} links, but got {len(demand_tag)}'
    context.app.total_projects_page.verify_info_buttons(high_demand_tag)'''


@then("Verify all products contain the High Demand tag")
def verify_high_demand_tag(context):
    count = 1
    while count < 13:
        context.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(1)
        context.driver.execute_script("window.scrollBy(0,2000)", "")

        all_products = context.driver.find_elements(*ALL_PRODUCTS)
        print("start Loop", count)

        for product in all_products:
            context.wait.until(EC.visibility_of_element_located(HIGH_DEMAND_TAG))
            title = product.find_element(*HIGH_DEMAND_TAG).text  # search each product and find the high demand tag

            print(title)
            assert title, 'product title not shown'  # this will assert that the high demand tag is shown in each tile and if not, will fail with 'product not shown' messag

        context.wait.until(EC.element_to_be_clickable(CLICK_NEXT_PAGE), message='next page button not clicked')
        context.driver.find_element(*CLICK_NEXT_PAGE).click()

        print("count", count)
        count += 1
