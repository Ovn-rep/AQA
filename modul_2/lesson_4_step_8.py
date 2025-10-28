import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 15)
link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser.get(link)

    price_text = wait.until(text_to_be_present_in_element((By.ID, "price"),"$100"))
    button_book = browser.find_element(By.ID, "book")
    button_book.click()

    chislo_place = browser.find_element(By.ID, "input_value")
    chislo = int(chislo_place.text)
    input_math = browser.find_element(By.ID, "answer")
    input_math.send_keys(calc(chislo))

    button_submit = browser.find_element(By.ID, "solve")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()


