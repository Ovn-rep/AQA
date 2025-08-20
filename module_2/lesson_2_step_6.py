from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/execute_script.html")
numtext = browser.find_element(by = "id", value = "input_value")
x = int(numtext.text)
result = calc(x)
input1 = browser.find_element(by = "id", value = "answer")
input1.send_keys(str(result))
checkbox = browser.find_element(by = "css selector", value = '[type="checkbox"]')
checkbox.click()
radio = browser.find_element(by = "id", value = 'robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()
button = browser.find_element(by = "tag name", value = 'button')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(10)
