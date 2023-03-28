import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# link = "https://stepik.org/lesson/236895/step/1"

@pytest.mark.parametrize('code', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_send_answer():
    link = f"https://stepik.org/lesson/{code}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.ID, "ember33").click()
    browser.find_element(By.ID, "id_login_email").send_keys("asokolov19996@gmail.com")
    browser.find_element(By.ID, "id_login_password").send_keys("A4/Hd2xjMasJi-9")
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
    answer = math.log(int(time.time()))
    browser.find_element(By.ID, "ember97").send_keys(answer)
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    time.sleep(10)