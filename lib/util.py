import time
from selenium import webdriver

def loginAndCheck(username, password):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get('http://127.0.0.1:8088/mgr/sign.html')

    if username is not None:
        driver.find_element_by_id('username').send_keys(username)

    if password is not None:
        driver.find_element_by_id('password').send_keys(password)

    driver.find_element_by_css_selector("button[type='submit']").click()

    time.sleep(2)

    alterText = driver.switch_to_alert().text
    print(alterText)

    driver.quit()

    return alterText


