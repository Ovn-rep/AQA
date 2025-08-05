import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/simple_form_find_task.html')

input1 = driver.find_element(by='tag name', value="input")
input1.send_keys("Ivan")
input2 = driver.find_element(by='name', value="last_name")
input2.send_keys("Petrov")
input3 = driver.find_element(by='class name',value="form-control.city")
input3.send_keys("Smolensk")
input4 = driver.find_element(by='id', value="country")
input4.send_keys("Russia")
button = driver.find_element(By.CSS_SELECTOR, value="button.btn")
button.click()
time.sleep(5)
