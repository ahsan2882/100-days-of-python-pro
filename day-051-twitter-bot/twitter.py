from selenium import webdriver
WEBDRIVER = webdriver.chrome.webdriver.WebDriver
By = webdriver.common.by.By


class InternetSpeedTwitterBot:
    def __init__(self, driver: WEBDRIVER, up, down):
        self.driver = driver
        self.up = up
        self.down = down

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')

    def tweet_at_provider(self):
        pass
