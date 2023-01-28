from pathlib import Path
from selenium import webdriver

ChromeService = webdriver.chrome.service.Service
By = webdriver.common.by.By

DRIVER_PATH = Path("C:/webdrivers/chromedriver.exe").resolve()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = ChromeService(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(
    By.CSS_SELECTOR, "#articlecount a").get_attribute('innerHTML')
print(article_count)

driver.quit()
