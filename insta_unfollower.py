import time
import secrets
from selenium.webdriver.common.by import By
from instagram_bot import InstagramBot
URL = "https://www.instagram.com/"


class InstaUnfollower(InstagramBot):
    def __init__(self):
        super().__init__()
        self.followers, self.following = [], []

    def login(self):
        super().login()

    def following_info(self):
        self.driver.get(f'{URL}{secrets.USERNAME}')
        time.sleep(2)
        self.driver.get(f'{URL}{secrets.USERNAME}/followers/')
        time.sleep(4)

        self.scrolling()
        self.followers = [item.text for item in self.driver.find_elements(
            By.CSS_SELECTOR, value="span._aacl._aaco._aacw._aacx._aad7._aade"
        )]
        print(len(self.followers))
        time.sleep(5)

        self.driver.get(f'{URL}{secrets.USERNAME}/following/')
        time.sleep(7)

        self.scrolling()
        self.following = [item.text for item in self.driver.find_elements(
            By.CSS_SELECTOR, value="span._aacl._aaco._aacw._aacx._aad7._aade"
        )]
        time.sleep(3)

    def scrolling(self):
        scroll = True
        while scroll:
            modal = self.driver.find_element(By.CLASS_NAME, "_aano")
            scroll_height = self.driver.execute_script("return arguments[0].scrollHeight", modal)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2.5)
            scroll_height_new = self.driver.execute_script("return arguments[0].scrollHeight", modal)
            if scroll_height_new == scroll_height:
                scroll = False

    def compare(self):
        for following in self.following:
            if following not in self.followers:
                print(f'@{following} is not following you back')
