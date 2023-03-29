import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


    @pytest.mark.parametrize('code', [
        "236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"
    ])

def test_send_answer(browser, code):
    answer = str(math.log(int(time.time())))
    link = f"https://stepik.org/lesson/{code}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element(By.ID, "ember33").click()
    browser.find_element(By.ID, "id_login_email").send_keys("asokolov19996@gmail.com")
    browser.find_element(By.ID, "id_login_password").send_keys("A4/Hd2xjMasJi-9")
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
    browser.find_element(By.ID, "ember97").send_keys(answer)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    feedback = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")).text
    )
    assert feedback == "Correct!", f"Unexpected feedback message: {feedback}"