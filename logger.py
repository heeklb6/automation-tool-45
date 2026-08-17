import logging

class Logger:
    def __init__(self, log_file='app.log'):
        # Set up the logger
        self.logger = logging.getLogger('CryptoLogger')
        self.logger.setLevel(logging.DEBUG)

        # Create file handler
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)

        # Create console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

        # Create a formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

# Example usage:
# logger = Logger()
# logger.info('This is an info message')
