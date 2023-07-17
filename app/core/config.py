import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from pydantic import BaseSettings

BASE_DIR = Path(__file__).parent.parent
LOGS_DIR = BASE_DIR / 'logs'
LOG_FILE = LOGS_DIR / 'fastapi_app.log'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
LOG_DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'


class Settings(BaseSettings):
    app_title: str = "Cargo Insurance"
    app_description: str = "Расчет стоимости страхования груза"

    class Config:
        env_file = '.env'


settings = Settings()


def configure_logging():
    """Описание конфигурации для логирования"""
    LOGS_DIR.mkdir(exist_ok=True)
    rotating_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=10**6, backupCount=5, encoding='utf-8',
    )

    logging.basicConfig(
        datefmt=LOG_DATETIME_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler,),
    )
