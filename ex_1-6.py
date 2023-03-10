from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import unittest

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/registration1.html"

try:
    browser.get(link)

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
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()