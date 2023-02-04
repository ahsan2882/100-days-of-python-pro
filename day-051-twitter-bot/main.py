import os
from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver
from twitter import InternetSpeedTwitterBot

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(),
    '.env'
).resolve()

load_dotenv(DOTENV_PATH)

PROMISED_DOWN = 200
PROMISED_UP = 100
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

ChromeService = webdriver.chrome.service.Service
By = webdriver.common.by.By
WEBDRIVER = webdriver.chrome.webdriver.WebDriver

DRIVER_PATH = Path("C:/webdrivers/chromedriver.exe").resolve()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
service = ChromeService(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)


twitterBot = InternetSpeedTwitterBot(
    driver=driver, up=PROMISED_UP, down=PROMISED_DOWN)

twitterBot.get_internet_speed()
