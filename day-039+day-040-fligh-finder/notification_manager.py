import smtplib
import os
from pathlib import Path
from dotenv import load_dotenv

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(),
    '.env'
).resolve()

load_dotenv(DOTENV_PATH)


EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            email_content = f"Subject:Low Price Alert\n\n{message}"
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=email_content.encode('utf-8'))
