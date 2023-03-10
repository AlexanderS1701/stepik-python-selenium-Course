from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class test_class_name(unittest.TestCase):

    def test_first(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("email@gmail.com")
        input4 = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
        input4.send_keys("+71234567898")
        input5 = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
        input5.send_keys("Kazakhstan")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!",\
                         welcome_text, "error")

    def test_second(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("email@gmail.com")
        input4 = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
        input4.send_keys("+71234567898")
        input5 = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
        input5.send_keys("Kazakhstan")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!",\
                         welcome_text, "error")

if __name__ == "__main__":
    unittest.main()