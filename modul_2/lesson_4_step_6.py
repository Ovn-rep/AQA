from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button1 = browser.find_element(by = "id", value = "book")
button1.click()
znachenie = browser.find_element(by = "id", value = "input_value")
x = int(znachenie.text)
y = calc(x)
input1 = browser.find_element(by = "id", value = "answer")
input1.send_keys(str(y))
button2 = browser.find_element(by = "id", value = "solve")
button2.click()

time.sleep(10)









