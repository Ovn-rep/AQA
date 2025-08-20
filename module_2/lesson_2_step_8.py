from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/file_input.html")

input1 = browser.find_element(by = "css selector", value = '[placeholder="Enter first name"]')
input1.send_keys('Aleksandr')
input2 = browser.find_element(by = "css selector", value = '[placeholder="Enter last name"]')
input2.send_keys('Karasev')
input3 = browser.find_element(by = "css selector", value = '[placeholder="Enter email"]')
input3.send_keys('alex333karasev@yandex.ru')
button1 = browser.find_element(by = "id", value = 'file')
directory = "/Users/akarasev/Desktop/"
file_name = "Privet.txt"
file_path = os.path.join(directory, file_name)
button1.send_keys(file_path)
button2 = browser.find_element(by = "tag name", value = 'button')
button2.click()

time.sleep(10)
