import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

class Test1(unittest.TestCase):
    def test_1(self):
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element(by="css selector", value='input[placeholder="Input your first name"]')
        input1.send_keys("Alex")
        input2 = browser.find_element(by="css selector", value='input[placeholder="Input your last name"]')
        input2.send_keys("Karasev")
        input3 = browser.find_element(by="css selector", value='input[placeholder="Input your email"]')
        input3.send_keys("alexx333karasev@yandex.ru")
        input4 = browser.find_element(by="css selector", value='input[placeholder="Input your phone:"]')
        input4.send_keys("+79261288070")
        input5 = browser.find_element(by="css selector", value='input[placeholder="Input your address:"]')
        input5.send_keys("Moscow")

        button = browser.find_element(by="tag name", value="button")
        button.click()
        time.sleep(1)

        massage = browser.find_element(by="tag name", value="h1")
        true_massage = massage.text

        self.assertEqual("Congratulations! You have successfully registered!", true_massage)

    def test_2(self):
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element(by="css selector", value='input[placeholder="Input your first name"]')
        input1.send_keys("Alex")
        input2 = browser.find_element(by="css selector", value='input[placeholder="Input your last name"]')
        input2.send_keys("Karasev")
        input3 = browser.find_element(by="css selector", value='input[placeholder="Input your email"]')
        input3.send_keys("alexx333karasev@yandex.ru")

        button = browser.find_element(by="tag name", value="button")
        button.click()
        time.sleep(1)

        massage = browser.find_element(by="tag name", value="h1")
        true_massage = massage.text

        self.assertEqual("Congratulations! You have successfully registered!", true_massage)

if __name__ == "__main__":
    unittest.main()
