from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import Select

ChromeService = webdriver.chrome.service.Service
By = webdriver.common.by.By
Keys = webdriver.common.keys.Keys

DRIVER_PATH = Path("C:/webdrivers/chromedriver.exe").resolve()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = ChromeService(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://formy-project.herokuapp.com/form")
driver.implicitly_wait(time_to_wait=3)
form = driver.find_element(By.TAG_NAME, "form")
first_name = form.find_element(By.ID, "first-name")
first_name.click()
first_name.send_keys("John")

last_name = form.find_element(By.ID, "last-name")
last_name.click()
last_name.send_keys("Doe")

job_title = form.find_element(By.ID, "job-title")
job_title.click()
job_title.send_keys("Software Developer")

education = form.find_element(By.ID, "radio-button-2")
education.click()

gender = form.find_element(By.ID, "checkbox-1")
gender.click()

experience = Select(form.find_element(By.ID, "select-menu"))
experience.select_by_visible_text("2-4")

date = form.find_element(By.ID, "datepicker")
date.click()
date.send_keys("02/01/2023")

form.submit()


driver.quit()
