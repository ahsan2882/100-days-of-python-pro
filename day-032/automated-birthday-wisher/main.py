from datetime import datetime
import smtplib
from pathlib import Path
import os
from dotenv import load_dotenv
import pandas as pd
from random import randint

LETTER_TEMPLATE_PATH = Path(
    Path(__file__).parent.resolve(), 'templates'
).resolve()

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(), '.env'
).resolve()
load_dotenv(DOTENV_PATH)
BIRTHDAY_CSV_PATH = Path(
    Path(__file__).parent.resolve(), 'birthdays.csv'
).resolve()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

now = datetime.now()
today = (now.month, now.day)

df = pd.read_csv(BIRTHDAY_CSV_PATH)
birthday_dict = {(data_row['month'], data_row['day'])
                  : data_row for (index, data_row) in df.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    name = birthday_person['name']
    email = birthday_person['email']
    letter_path = Path(LETTER_TEMPLATE_PATH,
                       f'letter_{randint(1, 3)}.txt').resolve()
    with open(letter_path) as f:
        letter = f.read()
        letter = letter.replace('[NAME]', name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{letter}")
