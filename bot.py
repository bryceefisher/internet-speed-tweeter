from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        self.service = Service("/Users/bryce/Desktop/Development/chromedriver")
        self.driver = webdriver.Chrome(service=self.service)
        self.up = ""
        self.down = ""
        self.TWITTER_USER = "Enter Twitter Username"
        self.TWITTER_PASS = "Enter Twitter Pass"

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        go.click()
        time.sleep(45)
        self.down = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div["
                                                       "3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        self.up = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div["
                                                     "3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(2)
        sign_in = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div["
                                                     "1]/div/div[ "
                                                     "3]/div[5]/a")
        sign_in.click()
        time.sleep(2)
        input_user = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div["
                                                        "2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div["
                                                        "2]/div/input")
        input_user.send_keys(self.TWITTER_USER)
        input_user.send_keys(Keys.ENTER)
        time.sleep(2)
        pass_input = self.driver.find_element(By.NAME, "password")
        pass_input.send_keys(self.TWITTER_PASS)
        pass_input.send_keys(Keys.ENTER)
        time.sleep(2)
        tweet_button = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div["
                                                "1]/div[3]/a/div")
        tweet_button.click()
        time.sleep(2)
        tweet = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div["
                                                   "2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div["
                                                   "1]/div/div/div/div/div/div[2]/div/div/div/div/label/div["
                                                   "1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet.send_keys(f"Hey @YourISP why is my internet speed Down: {self.down}mbps Up: {self.up}mbps when I pay for "
                        f"Down: Your Downmbps Up: Your Upmbps?")
        send_tweet = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div["
                                                        "2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div["
                                                        "3]/div/div/div[2]/div[4]")
        send_tweet.click()
