import logging

class AutomationTool:
    def __init__(self, name):
        self.name = name
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger(self.name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

    def run(self):
        self.logger.info('Starting automation tool')
        # Main automation logic here
        self.cleanup()

    def cleanup(self):
        self.logger.info('Cleaning up resources')
        # Cleanup logic here

if __name__ == '__main__':
    tool = AutomationTool('AutomationTool45')
    tool.run()