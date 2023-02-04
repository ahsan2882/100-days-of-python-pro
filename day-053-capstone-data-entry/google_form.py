import os
import random
from time import sleep
from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver
from fake_useragent import UserAgent
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(), ".env"
).resolve()
load_dotenv(DOTENV_PATH)

GOOGLE_FORM_URL = os.getenv("GOOGLE_FORM_URL")

ua = UserAgent()
userAgent = ua.random

ChromeService = webdriver.chrome.service.Service
By = webdriver.common.by.By
Keys = webdriver.common.keys.Keys
WEBDRIVER = webdriver.chrome.webdriver.WebDriver

DRIVER_PATH = Path("C:/webdrivers/chromedriver.exe").resolve()

options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={userAgent}')
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
service = ChromeService(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)


class GoogleForm:
    def __init__(self):
        self.google_form_url = GOOGLE_FORM_URL
        self.driver = webdriver.Chrome(service=service, options=options)

    def update_form(self, a_list, p_list, l_list):
        driver = self.driver
        driver.maximize_window()

        for i in range(len(l_list)):
            driver.get(self.google_form_url)
            sleep(1)
            first_answer = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div['
                                                         '2]/div/div[1]/div/div[1]/input')
            first_answer.send_keys(a_list[i])

            second_answer = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div['
                                                          '2]/div/div[1]/div/div[1]/input')
            second_answer.send_keys(p_list[i])

            third_answer = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div['
                                                         '2]/div/div[1]/div/div[1]/input')
            third_answer.send_keys(l_list[i])

            submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div['
                                                          '1]/div/span/span')
            submit_button.click()
            sleep_list = [0.1, 0.12, 0.15, 0.13]
            sleep(random.choice(sleep_list))
