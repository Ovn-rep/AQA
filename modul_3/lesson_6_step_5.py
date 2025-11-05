import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope = 'function')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.find_element(By.CLASS_NAME, "again-btn").click()
    browser.quit()


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class Test_auth():

    def test_1(self, browser, link):
        browser.get(link)
        wait = WebDriverWait(browser, 20)

        button_vis = wait.until(EC.visibility_of_element_located((By.ID, "ember483")))
        button_vis.click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "light-tabs")))

        input_email = wait.until(EC.visibility_of_element_located((By.ID, "id_login_email")))
        input_email.send_keys("alex333karasev@yandex.ru")
        input_password = wait.until(EC.visibility_of_element_located((By.ID, "id_login_password")))
        input_password.send_keys("OVNlBD161620!!!")
        button_auth = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "sign-form")))
        button_auth.click()

        wait.until_not(EC.visibility_of_element_located((By.CLASS_NAME, "light-tabs")))

        input_vis = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ember-text-area")))
        input_vis.send_keys(str(math.log(int(time.time()))))
        answer_button_vis = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        answer_button_vis.click()
        answer_text_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
        text = answer_text_element.text

        if text != 'Correct!':
            with open('result.txt', 'a') as file:
                file.write(text)

        assert text == "Correct!"









