import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


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
    link = f"https://stepik.org/lesson/{code}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)

    browser.find_element(By.CLASS_NAME, "navbar__auth_login").click()
    browser.find_element(By.ID, "id_login_email").send_keys("asokolov19996@gmail.com")
    browser.find_element(By.ID, "id_login_password").send_keys("A4/Hd2xjMasJi-9")
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
    time.sleep(5)

    textarea = browser.find_element(By.CSS_SELECTOR, "textarea")
    answer = str(math.log(int(time.time())))
    textarea.send_keys(answer)
    browser.find_element(By.CLASS_NAME, "submit-submission").click()

    feedback = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert feedback == "Correct!", f"Unexpected feedback message: {feedback}"