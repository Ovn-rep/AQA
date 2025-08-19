from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

image = browser.find_element(by = "tag name", value = "img")
x = int(image.get_attribute("valuex"))
result = math.log(abs(12 * math.sin(x)))
input1 = browser.find_element(by = "id", value = "answer")
input1.send_keys(str(result))
time.sleep(3)
checkbox = browser.find_element(by = "css selector", value = '[type="checkbox"]')
checkbox.click()
time.sleep(3)
radio = browser.find_element(by = "css selector", value = '[value="robots"]')
radio.click()
time.sleep(3)
button = browser.find_element(by = "tag name", value = "button")
button.click()

time.sleep(10)








