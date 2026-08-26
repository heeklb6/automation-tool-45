import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = "crypto_bot") -> logging.Logger:
    """Configure and return a rotating file logger for automation tasks."""
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    log_file = os.path.join(log_dir, "automation.log")
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        # File handler with 5MB rotation and 3 backups
        file_handler = RotatingFileHandler(
            log_file, maxBytes=5 * 1024 * 1024, backupCount=3
        )
        file_handler.setLevel(logging.INFO)
        
        # Console handler for real-time monitoring
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Standard formatting suitable for crypto operations
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger

logger = setup_logger()