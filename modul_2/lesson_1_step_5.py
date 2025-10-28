from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()

lst_fields = [[By.ID, "answer"],
              [By.ID, "robotCheckbox"],
              [By.ID, "robotsRule"],
              [By.CLASS_NAME, ".btn"]
]

def calc(x):
  return str(math.log10(abs(12 * math.sin(x))))


try:
  browser.get("https://suninjuly.github.io/math.html")

  chislo = browser.find_element(By.ID, "input_value")
  k = int(chislo.text)

  for method, locator_name in lst_fields:
    elements = browser.find_element(method, locator_name)
    if locator_name == "answer":
      elements.send_keys(calc(k))
    else:
      elements.click()

finally:
  time.sleep(10)
  browser.quit()
