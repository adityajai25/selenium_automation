from selenium.webdriver.common.by import By

from base.webdriver_wrapper import AutomationWrapper


class TestAddEmployee(AutomationWrapper):

    def test_add_valid_employee(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")

        self.driver.find_element(By.NAME, "password").send_keys("admin123")

        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()

        # click on PIM menu

        # click on add employee

        # enter firstname as john

        # enter middle name as j

        # enter lastname as wick

        #  click on save

        # assert the profile name - john wick
