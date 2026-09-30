import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = 'automation.log') -> logging.Logger:
    """Initializes a rotating logger for crypto operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Ensure logs directory exists
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Setup rotating file handler: 5MB per file, keep 3 backups
    file_path = os.path.join(log_dir, log_file)
    handler = RotatingFileHandler(
        file_path, 
        maxBytes=5*1024*1024, 
        backupCount=3
    )

    # Formatter for timestamps and log levels
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    # Optional console stream for development
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger