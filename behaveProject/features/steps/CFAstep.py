import random
import string
import time

from behave import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome, ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
region = "TestCFA1" + str(random.randint(0, 999))

@given(u'User is on STEP Login page')
def step_impl(context):
    options = ChromeOptions()
    options.add_experimental_option("detach", True)
    context.driver = Chrome(service=Service("C:/Chrome driver/chromedriver.exe"), options=options)
    context.driver.implicitly_wait(5)
    context.driver.maximize_window()
    context.driver.get("https://chick-fil-a-preprod.scloud.stibo.com/")

@when('user Enters Username')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("FIELDOPSTEST")

@when(u'user Enters Password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("FIELDOPSTEST")

@when(u'user click on Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='kc-login']").click()

@when(u'user click on location user portal WebUi')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                        "//a[@href='/webui/CFAUserPortal']//div[@class='webui-icon']//img[@alt='webui_icon']").click()

@when(u'after succesfull login user click on link Create New Region on widget')
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH, "//div[normalize-space()='Create New Region']").click()


@when(u'user enters Region Name and user clicks on next button')
def step_impl(context):
    time.sleep(5)
    # region name

    context.driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(region)
    context.driver.find_element(By.CSS_SELECTOR, ".text").click()


@when(u'user navigates to "region details page"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR,
                        "input[class='gwt-TextBox stibo-Value-ISO-Date stibo-Value mandatory-for-approval mandatory validator-isodate']").click()


@when(u'user enters Start Date in Region Details page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//*[text()='25'])[1]").click()
    time.sleep(5)


@when(u'user clicks on Create button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR,
                        "button[class='stibo-GraphicsButton material SubmitButton'] span[class='text']").click()


@then(u'confirmation pop-up is displayed')
def step_impl(context):
    print("AP")


@given(u'User is on location user portal page')
def step_impl(context):
    options = ChromeOptions()
    options.add_experimental_option("detach", True)
    context.driver = Chrome(service=Service("C:/Chrome driver/chromedriver.exe"), options=options)
    context.driver.get("https://chick-fil-a-preprod.scloud.stibo.com/")
    context.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("FIELDOPSTEST")
    context.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("FIELDOPSTEST")
    context.driver.find_element(By.XPATH, "//input[@id='kc-login']").click()
    context.driver.find_element(By.XPATH,
                        "//a[@href='/webui/CFAUserPortal']//div[@class='webui-icon']//img[@alt='webui_icon']").click()


@when(u'user click on link "Create New Area Support Team" on widget')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element(By.CSS_SELECTOR,
                        "div[id='Create_Area_Support_Team'] div div[class='gwt-Label status-selector__initiate-link-wrapper']").click()


@when(u'user click on node in text field of "Parent Region Node" to select region names')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//i[@class='material-icons NodePickerIcon']").click()


@when(u'user selects parent region node from search option')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//div[@role='tab']//div[@class='gwt-Label'][normalize-space()='Search']").click()


@when(u'user enters <Area Support Team Name>')
def step_impl(context, region=region):
    time.sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "input[class='gwt-SuggestBox']").send_keys(region)
    context.driver.find_element(By.CSS_SELECTOR,
                        "button[class='stibo-GraphicsButton material SearchButton'] span[class='text']").click()
    time.sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, "button[class='stibo-GraphicsButton'] span[class='text']").click()

    teamname = "testteamname"+str(random.randint(0,999))
    context.driver.find_element(By.CSS_SELECTOR, "input[class='gwt-TextBox stibo-StateFlow-Unbound-Variable stibo-Value stibo-Value-Text mandatory']").send_keys(teamname)

@when(u'user click on "Next" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".text").click()

@then(u'user should see successful message <pop-up>')
def step_impl(context):
    print("AK")


@when(u'user enters <Area Support Team Code> in general attributes tab')
def step_impl(context):
    time.sleep(5)
    res = ''.join(random.choice(string.ascii_letters) for i in range(1))
    teamcode = res + str(random.randint(0, 9))
    context.driver.find_element(By.XPATH,
                        "//input[@class='gwt-TextBox stibo-StateFlow-Unbound-Variable stibo-Value stibo-Value-Text mandatory']").send_keys(
        teamcode)


@when(u'user enters <Area Support Team Type> in general attributes tab')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR,
                        "[class='dropdown stibo-Value validator-text mandatory-for-approval stibo-Value-Text mandatory']").click()
    context.driver.find_element(By.XPATH, "//*[text()='Traditional']").click()


@when(u'user enters <Start Date> in general attributes tab')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                        "(//input[@class='gwt-TextBox stibo-Value-ISO-Date stibo-Value mandatory-for-approval mandatory validator-isodate'])[1]").click()
    context.driver.find_element(By.XPATH, "(//*[text()='27'])[1]").click()


@when(u'user enters <Assignment Start Date> in general attributes tab')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH,
                        "(//input[@class='gwt-TextBox stibo-Value-ISO-Date stibo-Value mandatory-for-approval mandatory validator-isodate'])[2]").click()
    context.driver.find_element(By.XPATH, "//*[text()='27']").click()


@when(u'user selects Active Area Support Team Roles tab')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR,
                        "div[id='stibo_tab_Active_Area_Support_Team_Roles'] div[class='tabs-panel-tab-inner'] div span[class='gwt-InlineLabel']").click()
    time.sleep(10)

@when(u'user click on "Add roles" select <Reference Type> and <Reference Target>')
def step_impl(context):
    #select add role
    listofelement = context.driver.find_elements(By.CSS_SELECTOR, "[title='Create a new reference']")
    listofelement[0].click()
    context.driver.find_element(By.CSS_SELECTOR, "[class='material-icons add-reference']").click()
    #select director
    context.driver.find_element(By.CSS_SELECTOR, "[id='tree_expanded_node_StaffRoot']").click()
    time.sleep(10)
    listoftarget= context.driver.find_elements(By.CSS_SELECTOR, "[class='treeRow ']")
    print(len(listoftarget))
    listoftarget[3].click()
    context.driver.find_element(By.XPATH, "(//span[@class='text'][normalize-space()='OK'])[2]").click()
    context.driver.find_element(By.CSS_SELECTOR, "button[class='stibo-GraphicsButton'] span[class='text']").click()
    #select add role
    listofelement2 = context.driver.find_elements(By.CSS_SELECTOR, "[title='Create a new reference']")
    listofelement2[0].click()
    context.driver.find_element(By.CSS_SELECTOR, ".stibo-Dropdown.FormFieldWidget").click()
    context.driver.find_element(By.CSS_SELECTOR, "[value='Region Lead']").click()
    #select region lead
    context.driver.find_element(By.CSS_SELECTOR, "[class='material-icons add-reference']").click()
    context.driver.find_element(By.CSS_SELECTOR, "[id='tree_expanded_node_StaffRoot']").click()
    time.sleep(3)
    listoftarget2 = context.driver.find_elements(By.CSS_SELECTOR, "[class='treeRow ']")
    listoftarget2[1].click()
    context.driver.find_element(By.XPATH, "(//span[@class='text'][normalize-space()='OK'])[2]").click()
    context.driver.find_element(By.CSS_SELECTOR, "button[class='stibo-GraphicsButton'] span[class='text']").click()

@when(u'user selects "Assignment start date" for each role')
def step_impl(context):
    print("PK")


@when(u'user clicks on "Create" button')
def step_impl(context):
    print("AB")


@then(u'user should see successful message <pop-up> on dashboard')
def step_impl(context):
    print("HB")