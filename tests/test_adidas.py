import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


class TestSemanticsTopvisor(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        # Driver setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def test_accept_cookie(self):
        self.driver.get("https://www.adidas.fi/")
        cookie = self.driver.find_element(By.XPATH, "//button[@id='glass-gdpr-default-consent-accept-button']")
        cookie.click()

    def test_check_page_title(self):
        self.driver.get("https://www.adidas.fi/")
        self.assertEqual("adidas Official Website FI | Sportswear", self.driver.title)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()