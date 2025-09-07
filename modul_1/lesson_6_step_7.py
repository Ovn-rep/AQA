from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/huge_form.html"
    browser.get(link)

    elements = browser.find_elements(by = "tag name", value="input")
    for element in elements:
        element.send_keys('Privet')

    button = browser.find_element(by = "class name", value='btn.btn-default')
    button.click()

    time.sleep(20)
finally:
    browser.quit()