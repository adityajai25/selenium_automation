from assertpy import assert_that

from base.webdriver_wrapper import AutomationWrapper
from selenium.webdriver.common.by import By

class TestLogin(AutomationWrapper):
    def test_valid_login(self):
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        self.driver.find_element(By.CLASS_NAME,"oxd-button").click()
        actual_text = self.driver.find_element(By.XPATH,"//p[contains(normalize-space(),'Quick')]").text
        assert_that("Quick Launch").is_equal_to(actual_text)
