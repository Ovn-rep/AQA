from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_user_can_see_add_to_basket(browser):
    wait = WebDriverWait(browser, 10)
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary"))), 'No element on the page'
    time.sleep(30)