import os
import logging
from logging.handlers import RotatingFileHandler

# Configure the logger
LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_FILE = 'crypto_tool.log'
MAX_BYTES = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3


def setup_logger():
    logger = logging.getLogger('CryptoAutomationTool')
    logger.setLevel(LOGGING_LEVEL)
    handler = RotatingFileHandler(LOG_FILE, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
    formatter = logging.Formatter(LOGGING_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Example usage:
if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger is set up and ready.')