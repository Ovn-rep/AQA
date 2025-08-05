from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_xpath_form")

input1 = browser.find_element(by = "tag name", value = "input")
input1.send_keys("Aleksandr")
input2 = browser.find_element(by = "name", value = "last_name")
input2.send_keys('Karasev')
input3 = browser.find_element(by = "class name", value = "form-control.city")
input3.send_keys("Ramenskoe")
input4 = browser.find_element(by = "css selector", value = "input#country")
input4.send_keys('Russia')

button = browser.find_element(by = "xpath", value = '//button[text()="Submit"]')
button.click()

time.sleep(1)