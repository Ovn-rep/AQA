from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button1 = browser.find_element(by = "class name", value = "btn.btn-primary")
    button1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    znachenie = browser.find_element(by = "id", value = "input_value")
    x = int(znachenie.text)
    y = calc(x)
    input1 = browser.find_element(by = "id", value = "answer")
    input1.send_keys(str(y))
    button2 = browser.find_element(by = "class name", value = "btn.btn-primary")
    button2.click()

    time.sleep(10)

finally:
    browser.quit()
