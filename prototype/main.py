from fastapi import FastAPI

from api_router import router

from logging_config import setup_logging

setup_logging()

app = FastAPI()

app.include_router(router)