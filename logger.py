import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger(logger_name: str = "crypto_automation", log_dir: str = "logs", max_size_mb: int = 5, backup_count: int = 3) -> logging.Logger:
    """Set up a logger with rotating file handler."""
    # Ensure log directory exists
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    log_file = log_path / f"{logger_name}.log"
    logger = logging.getLogger(logger_name)
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.setLevel(logging.INFO)
    # Rotating file handler for log rotation
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=max_size_mb * 1024 * 1024,
        backupCount=backup_count
    )
    file_formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    # Console handler for immediate feedback
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(file_formatter)
    logger.addHandler(console_handler)
    return logger

# Example usage in crypto automation context
if __name__ == "__main__":
    logger = setup_logger()
    logger.info("Starting crypto automation tool")
    logger.warning("Sample warning for testing rotation")
    # Simulate logging to trigger rotation if needed
    for i in range(10):
        logger.debug(f"Processing crypto transaction {i}")