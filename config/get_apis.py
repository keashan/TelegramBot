import os
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass

load_dotenv(find_dotenv())


@dataclass(frozen=True)
class Config:
    API_KEY: str = os.getenv("Telegram_API_KEY")
