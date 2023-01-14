from datetime import datetime
import smtplib
from pathlib import Path
import os
from dotenv import load_dotenv

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(), '.env'
).resolve()
load_dotenv(DOTENV_PATH)
