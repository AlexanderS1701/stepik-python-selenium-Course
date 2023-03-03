import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    '''ожидание'''
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()

    '''решение'''
    x = browser.find_element(By.ID, "input_value").text
    def calc(num):
        return str(math.log(abs(12*math.sin(int(num)))))
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(4)
    browser.quit()