import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/simple_form_find_task.html')

    input1 = browser.find_element(by='tag name', value="input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(by='name', value="last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(by='class name',value="form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(by='id', value="country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    button.click()
    time.sleep(5)

finally:
    browser.quit()
