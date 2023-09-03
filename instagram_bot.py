import time
import secrets
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
URL = "https://www.instagram.com/"


class InstagramBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(URL)
        self.driver.maximize_window()
        # Give time for page to load
        time.sleep(2)
        self.login()

    def login(self):
        username_entry = self.driver.find_element(By.NAME, value="username")
        password_entry = self.driver.find_element(By.NAME, value="password")

        username_entry.send_keys(secrets.USERNAME)
        password_entry.send_keys(secrets.PASSWORD)
        password_entry.send_keys(Keys.ENTER)

        # Wait for any verification prompt
        try:
            time.sleep(5)
            save_info_button = self.driver.find_element(By.CSS_SELECTOR, value="._aa56 button")
            save_info_button.click()

            time.sleep(1)
            not_now_button = self.driver.find_element(By.CLASS_NAME, value="_a9_1")
            not_now_button.click()
        except NoSuchElementException:
            pass
