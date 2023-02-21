import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("okrens46@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("asustuf123") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "signin_login").click()
        time.sleep(1)
        

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
