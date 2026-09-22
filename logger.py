import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'crypto_bot', log_file: str = 'automation.log'):
    """
    Configures a rotating file logger for crypto automation tool.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-initialized
    if logger.handlers:
        return logger

    # Define log format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # File rotation: 5MB per file, keep 5 backups
    file_handler = RotatingFileHandler(
        log_file, 
        maxBytes=5*1024*1024, 
        backupCount=5
    )
    file_handler.setFormatter(formatter)

    # Console output handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Instantiate default logger for the module
logger = setup_logger()