from pathlib import Path
from selenium import webdriver

ChromeService = webdriver.chrome.service.Service
By = webdriver.common.by.By

DRIVER_PATH = Path("C:/webdrivers/chromedriver.exe").resolve()


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = ChromeService(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
driver.implicitly_wait(3)


events = {str(time.find_element(By.CSS_SELECTOR,
                                "span.say-no-more").get_attribute(name="innerHTML") + time.text): str(name.text) for time, name in zip(event_times, event_names)}

print(events)

driver.quit()
