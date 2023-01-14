from datetime import datetime
import smtplib
from pathlib import Path
import os
from dotenv import load_dotenv
from random import choice

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(), '.env'
).resolve()
load_dotenv(DOTENV_PATH)

DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']

TEXT_FILE_PATH = Path(
    Path(__file__).parent.resolve(),
    'quotes.txt'
).resolve()

with open(TEXT_FILE_PATH) as f:
    quotes = f.readlines()

random_quote = choice(quotes)

now = datetime.now()
day_of_week = now.weekday()

email = "ahsan.shahid.cssfl@gmail.com"
password = os.getenv('PASSWORD')

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs="ahsanshahid2882@gmail.com",
                        msg=f"Subject:Motivational Quote for {DAYS_OF_WEEK[day_of_week]}\n\n{random_quote}")
