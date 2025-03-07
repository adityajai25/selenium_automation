from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.webdriver_wrapper import AutomationWrapper


class TestLoginUI(AutomationWrapper):
    def test_title(self):
        assert_that("OrangeHRM").is_equal_to(self.driver.title)

    def test_header(self):
        actual_header = self.driver.find_element(By.XPATH,"//h5").text
        assert_that("Login").is_equal_to(actual_header)
