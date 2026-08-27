from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


from fastapi import FastAPI

from api_router import router

from logging_config import setup_logging


setup_logging()

app = FastAPI()

app.include_router(router)