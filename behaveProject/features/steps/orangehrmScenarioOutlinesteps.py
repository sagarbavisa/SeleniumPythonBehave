from behave import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I Launch chrome browser')
def step_impl(context):
    options = ChromeOptions()
    options.add_experimental_option("detach", True)
    context.driver = Chrome(service=Service("C:/Chrome driver/chromedriver.exe"), options=options)


@when('I open orange hrm Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com")


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    wait = WebDriverWait(context.driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
    username_field.send_keys(user)
    password_field.send_keys(pwd)


@when('Click on login button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_button.click()


@then('User must successfully login to the Dashboard page')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        dashboard = wait.until(EC.presence_of_element_located((By.XPATH, "//h6[normalize-space()='Dashboard']")))
    except:
        context.driver.quit()
        assert False, "Test Failed"

    if dashboard.text == "Dashboard":
        context.driver.quit()
        assert True, "Test Passed"
