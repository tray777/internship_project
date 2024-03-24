from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context,scenario_name):
    """
    :param context: Behave context
    """
    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### OTHER BROWSERS ###
    # service = Service(executable_path='C:/Users/Owner/internship_project/geckodriver.exe')
    # context.driver = webdriver.Firefox(service=service)

    ### HEADLESS MODE ###
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument("window-size=1920,1080")
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(options=options, service=service)

    ### BROWSER STACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    #https://www.browserstack.com/docs/automate/capabilitieshttps://www.browserstack.com/docs/automate/capabilities
    bs_user = 'tracyarispe_Z6z07g'
    bs_key = 'gAWUTkUZbmoJSfwuego7'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "browserVersion": "latest",
        'os': 'OS X',
        'osVersion': 'Ventura',
        'browserName': 'Chrome',
        "consoleLogs": "info",
        #"deviceName": "",
        'sessionName': scenario_name
    }

    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    #context.driver.implicitly_wait(4)

    context.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context,scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
