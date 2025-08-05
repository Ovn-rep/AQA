import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")
time.sleep(2)

url = browser.find_element(by = 'link text', value=str(math.ceil(math.pow(math.pi, math.e)*10000)))
url.click()
time.sleep(2)


input1 = browser.find_element(by = 'tag name', value = 'input')
input1.send_keys('Aleksandr')
input2 = browser.find_element(by = 'name', value = 'last_name')
input2.send_keys('Karasev')
input3 = browser.find_element(by='class name',value="form-control.city")
input3.send_keys("Smolensk")
input4 = browser.find_element(by='id', value="country")
input4.send_keys("Russia")
button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
button.click()

time.sleep(3)

print('Тест успешно завершен')

