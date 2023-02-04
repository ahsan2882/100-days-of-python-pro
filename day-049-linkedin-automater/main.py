import os
from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(),
    '.env'
).resolve()

load_dotenv(DOTENV_PATH)

LINKEDIN_EMAIL = os.getenv('LINKEDIN_EMAIL')
LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')
