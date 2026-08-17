import logging

# Configure the logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

def log_info(message):
    """Log an info message"""
    logger.info(message)


def log_warning(message):
    """Log a warning message"""
    logger.warning(message)


def log_error(message):
    """Log an error message"""
    logger.error(message)


def log_critical(message):
    """Log a critical message"""
    logger.critical(message)


def log_exception(exception):
    """Log an exception message"""
    logger.exception('An exception occurred: %s', exception)