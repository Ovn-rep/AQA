from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

lst_field = [
        ["first_name", By.NAME, "Alex"],
        ["last_name", By.NAME, "Karasev"],
        ["form-control.city", By.CLASS_NAME, "Moscow"],
        ["country", By.ID, "Russia"]
]

try:
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")

    for locator_name, locator_method, field_value in lst_field:
        elements = browser.find_element(locator_method, locator_name)
        elements.send_keys(field_value)

    button_1 = browser.find_element(By.ID, "submit_button")
    button_1.click()

finally:
    time.sleep(30)
    browser.quit()
