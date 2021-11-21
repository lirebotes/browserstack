import time
from selenium.webdriver.common.keys import Keys

@given('my username is "{username}"')
def step(context, username):
    context.username = username

@given('my password is "{password}"')
def step(context, password):
    context.password = password

@when('I visit url "{url}"')
def step(context, url):
    context.browser.get(url)

@when('field with name "{selector}" is given "{value}"')
def step(context, selector, value):
    elem = context.browser.find_element_by_name(selector)
    elem.send_keys(value)
    elem.submit()
    time.sleep(5)
    
@when('I sign in')
def step(context):
    context.browser.find_element_by_id("signin").click()
    time.sleep(5) #TODO: replace with expected_conditions
    context.browser.find_element_by_id("react-select-2-input").send_keys(context.username)
    context.browser.find_element_by_id("react-select-2-input").send_keys(Keys.ENTER)
    context.browser.find_element_by_id("react-select-3-input").send_keys(context.password)
    context.browser.find_element_by_id("react-select-3-input").send_keys(Keys.ENTER)
    context.browser.find_element_by_id("login-btn").click()
    
@then('title is "{title}"')
def step(context, title):
    assert context.browser.title == title

@then(u'the page contains "{body}"')
def step(context, body):
    assert body in context.browser.page_source
