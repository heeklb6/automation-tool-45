import logging
import os
import sys
from logging.handlers import RotatingFileHandler

def setup_logger(name: str, log_filepath: str = "logs/app.log", level: int = logging.INFO) -> logging.Logger:
    """
    Sets up a robust logger with a fallback to stdout if file writing fails.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Avoid duplicate handlers if logger is already configured
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler is always active as a baseline fallback
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Attempt file logger setup, catch permission and filesystem issues
    try:
        log_dir = os.path.dirname(log_filepath)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
            
        file_handler = RotatingFileHandler(
            log_filepath, maxBytes=10485760, backupCount=5, encoding='utf-8'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except (PermissionError, FileNotFoundError, OSError) as e:
        logger.warning(f"Failed to initialize file logger at {log_filepath} due to: {e}. Falling back to console logging.")

    return logger