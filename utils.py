import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = "automation_tool") -> logging.Logger:
    """
    Configures and returns a logger with rotating file and stream handlers.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Prevent duplicate handlers if the logger is initialized multiple times
    if not logger.handlers:
        log_format = logging.Formatter(
            "[%(asctime)s] %(levelname)s [%(name)s:%(filename)s:%(lineno)d] - %(message)s"
        )
        
        # Ensure the log directory exists in the environment
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, "crypto_bot.log")
        
        # Rotate log file at 5MB limit, keeping up to 5 historic log backups
        file_handler = RotatingFileHandler(
            log_file, maxBytes=5 * 1024 * 1024, backupCount=5, encoding="utf-8"
        )
        file_handler.setFormatter(log_format)
        file_handler.setLevel(logging.INFO)
        
        # Add a console stream handler for immediate terminal feedback
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_format)
        console_handler.setLevel(logging.INFO)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger