from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x, y):
    return(x + y)

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/selects1.html")

    num1 = browser.find_element(by = "id", value = "num1")
    x = int(num1.text)
    num2 = browser.find_element(by = "id", value = "num2")
    y = int(num2.text)
    result = calc(x, y)
    select = Select(browser.find_element(by = "id", value = "dropdown"))
    select.select_by_value(str(result))
    browser.find_element(by = "tag name", value = "button").click()

    time.sleep(10)

finally:
    browser.quit()







