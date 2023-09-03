import time
import secrets
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from instagram_bot import InstagramBot
URL = "https://www.instagram.com/"


class InstaFollower(InstagramBot):
    def __init__(self):
        super().__init__()
        time.sleep(2)
        self.login()

    def login(self):
        super().login()
        time.sleep(2)
        self.find_followers()

    def find_followers(self):
        self.driver.get(f'{URL}{secrets.ACCOUNT}/followers/')
        time.sleep(5)

        modal = self.driver.find_element(By.CLASS_NAME, value="_aano")

        while True:
            self.follow()
            self.driver.execute_script("arguments[0].scrollTop += arguments[0].offsetHeight;", modal)
            time.sleep(2)

    def follow(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")
        for button in buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/'
                                                                         'div/div/div/div/button[2]')
                cancel_button.click()
        buttons.clear()
