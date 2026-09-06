import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = "crypto_bot", log_file: str = "logs/app.log") -> logging.Logger:
    """
    Configures and returns a logger with both console and rotating file handlers.
    Automatically creates the log directory if it does not exist.
    """
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is already initialized
    if logger.handlers:
        return logger

    # Format output with timestamps, levels, and source modules
    log_format = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Rotating file handler (limit size to 5MB, keep up to 3 backup files)
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setFormatter(log_format)
    file_handler.setLevel(logging.INFO)

    # Stream handler for standard stdout output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    console_handler.setLevel(logging.INFO)

    # Attach handlers to the logger instance
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger