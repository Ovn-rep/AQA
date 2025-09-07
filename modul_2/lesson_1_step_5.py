from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  result = math.log(abs(12 * math.sin(int(x))))
  return result

browser = webdriver.Chrome()

try:
  browser.get('https://suninjuly.github.io/math.html')

  text_element = browser.find_element(by = "id", value = 'input_value')
  x = text_element.text
  y = calc(x)

  input1 = browser.find_element(by = "tag name", value = "input")
  input1.send_keys(str(y))
  checkbox = browser.find_element(by = "id", value="robotCheckbox")
  checkbox.click()
  radio = browser.find_element(by = "id", value="robotsRule")
  radio.click()

  button = browser.find_element(by = "class name", value = "btn.btn-default")
  button.click()

  time.sleep(10)

finally:
  browser.quit()
