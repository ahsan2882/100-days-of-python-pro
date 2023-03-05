import os
import time
import smtplib
from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(),
    '.env'
).resolve()

load_dotenv(DOTENV_PATH)

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

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


def sendEmail(message: str):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        email_content = f"Subject:Cookie Alert\n\n{message}"
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=email_content.encode('utf-8'))


def getCurrentProducers(driver: WEBDRIVER) -> dict:
    prod = {}
    all_producers = driver.find_elements(
        By.CSS_SELECTOR, '#products .product.unlocked')
    for producer in all_producers:
        try:
            name = producer.find_element(
                By.CSS_SELECTOR, '.content .title.productName').text
            quantity = int(producer.find_element(
                By.CSS_SELECTOR, '.content .title.owned').text)
            if quantity > 0:
                prod[name] = quantity
        except:
            pass
    return prod


driver.get('https://orteil.dashnet.org/cookieclicker/')

while True:
    try:
        driver.find_element(By.ID, 'langSelect-EN').click()
        break
    except:
        pass

timeout = time.time() + 1
send_email = time.time() + 60*60  # 1 hour
close_notes_period = time.time() + 10  # 10 seconds

while True:
    try:
        bigCookie = driver.find_element(By.ID, 'bigCookie')
        break
    except:
        pass

while True:
    try:
        driver.find_element(By.ID, 'storeBulk10').click()
        break
    except:
        pass


luckyCount = 0
upgrades_count = 0
producers = {}
error_count = 0
while True:
    if error_count > 10:
        sendEmail()
        driver.quit()
        break
    try:
        try:
            driver.find_element(By.LINK_TEXT, 'Got it!').click()
        except:
            pass
        try:
            bigCookie.click()
        except:
            bigCookie = driver.find_element(By.ID, 'bigCookie')
            bigCookie.click()
        try:
            shimmer = driver.find_element(
                By.CSS_SELECTOR, '#shimmers .shimmer')
            shimmer.click()
            luckyCount += 1
            print("Got lucky!")
        except:
            pass
        try:
            upgrade = driver.find_element(
                By.CSS_SELECTOR, '#upgrades .crate.upgrade.enabled')
            upgrade.click()
            upgrades_count += 1
            print('Bought an upgrade!')
        except:
            pass
        if time.time() > timeout:
            all_prices = driver.find_elements(
                By.CSS_SELECTOR, '#products .product.unlocked.enabled')
            if len(all_prices) == 0:
                all_prices = driver.find_elements(
                    By.CSS_SELECTOR, '#products .product.unlocked.enabled')
            try:
                highest_price = all_prices[-1]
                highest_price.click()
                buy_item = highest_price.find_element(
                    By.CSS_SELECTOR, '.content .title.productName').text
                print(f'Bought 10 {buy_item}s')
                all_prices.remove(highest_price)
            except:
                pass
            while len(all_prices) > 0:
                try:
                    highest_price = all_prices[-1]
                    highest_price.click()
                    buy_item = highest_price.find_element(
                        By.CSS_SELECTOR, '.content .title.productName').text
                    print(f'Bought 10 {buy_item}s')
                    all_prices.remove(highest_price)
                except:
                    pass
                all_prices = driver.find_elements(
                    By.CSS_SELECTOR, '#products .product.unlocked.enabled')
                if len(all_prices) == 0:
                    break

            timeout = time.time() + 1
        if time.time() > close_notes_period:
            try:
                driver.find_element(
                    By.CSS_SELECTOR, '#notes .note .close').click()
            except:
                pass
            close_notes_period = time.time() + 10
        if time.time() > send_email:
            num_cookies_text = driver.find_element(
                By.CSS_SELECTOR, '#cookies.title').text
            producers = getCurrentProducers(driver)
            producers_text = ''
            for (key, value) in producers.items():
                producers_text += f'{value} {key}s, '
            message = f"Cookie Clicker\nYou have reached {num_cookies_text}.\nYou have clicked {luckyCount} lucky cookies.\nYou have bought {upgrades_count} upgrades.\nYou have {producers_text}.\n"
            sendEmail(message)
            send_email = time.time() + 60*60
    except Exception as e:
        error_count += 1
        print(e)

# driver.get('https://orteil.dashnet.org/experiments/cookie/')
