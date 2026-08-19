from pathlib import Path

import logging

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def setup_logging():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        handlers=[
            logging.FileHandler(
                LOG_DIR / "app.log",
                encoding="utf-8"
            ),
            logging.StreamHandler()
        ],
        force=True
    )