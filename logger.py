import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = "automation-tool-45") -> logging.Logger:
    """Configures a rotating file logger for crypto operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not os.path.exists("logs"):
        os.makedirs("logs")

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Setup rotating file handler: 5MB per file, keep 5 backups
    file_handler = RotatingFileHandler(
        filename="logs/app.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5
    )
    file_handler.setFormatter(formatter)

    # Setup console handler for visibility
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger