import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    service = Service(r"C:\Users\bjon6\Sample_Automation\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver 
    driver.quit()

def test_case1(driver): #Positive LogIn test
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    WebDriverWait(driver, 10).until(EC.url_contains("logged-in-successfully"))

    assert "logged-in-successfully" in driver.current_url
    assert "Congratulations" in driver.page_source or "successfully logged in" in driver.page_source

    logout_button = driver.find_element(By.LINK_TEXT, "Log out")
    assert logout_button.is_displayed()

def test_case2(driver): #Negative username test
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    driver.find_element(By.ID, "username").send_keys("incorrectUser")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    assert "Your username is invalid!" in driver.find_element(By.ID, "error").text

def test_case3(driver): #Negative password test
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("incorrectPassword")
    driver.find_element(By.ID, "submit").click()

    assert "Your password is invalid!" in driver.find_element(By.ID, "error").text




