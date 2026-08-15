import logging
from logging.handlers import RotatingFileHandler

# Setup a logger for the application

def setup_logger(log_file='app.log', max_bytes=5*1024*1024, backup_count=3):
    """Setup the logger with rotation"""
    logger = logging.getLogger('crypto_logger')
    logger.setLevel(logging.DEBUG)  # Set the desired logging level

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    logger = setup_logger()  # Initialize the logger
    logger.info('Logger is set up with rotation')
    logger.error('This is an error message')
    logger.debug('This is a debug message')