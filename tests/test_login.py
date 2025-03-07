import pytest
from assertpy import assert_that
import pytest
from base.webdriver_wrapper import AutomationWrapper
from selenium.webdriver.common.by import By
from utilities.data_source import DataSource

class TestLogin(AutomationWrapper):
    def test_valid_login(self):
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        self.driver.find_element(By.CLASS_NAME,"oxd-button").click()
        actual_text = self.driver.find_element(By.XPATH,"//p[contains(normalize-space(),'Quick')]").text
        assert_that("Quick Launch").is_equal_to(actual_text)

    @pytest.mark.parametrize("username,password,expected_error",DataSource.test_invalid_login)
    def test_invalid_login(self,username,password,expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "oxd-button").click()
        actual_text = self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Invalid')]").text
        assert_that(expected_error).is_equal_to(actual_text)

    @pytest.mark.parametrize("username,password,expected_error",DataSource.test_invalid_login_csv)
    def test_invalid_login_csv(self,username,password,expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "oxd-button").click()
        actual_text = self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Invalid')]").text
        assert_that(expected_error).is_equal_to(actual_text)

    @pytest.mark.parametrize("username,password,expected_error", DataSource.test_invalid_login_excel)
    def test_invalid_login_excel(self, username, password, expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "oxd-button").click()
        actual_text = self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Invalid')]").text
        assert_that(expected_error).is_equal_to(actual_text)
