import os

class Config:
    """Configuration settings for the application."""
    def __init__(self):
        self.environment = os.getenv('ENVIRONMENT', 'development')
        self.debug = self.environment == 'development'
        self.database_uri = os.getenv('DATABASE_URI')
        self.log_level = os.getenv('LOG_LEVEL', 'INFO')
        self.port = int(os.getenv('PORT', 5000))

    def display_config(self):
        """Display the current configuration settings."""
        return {
            'environment': self.environment,
            'debug': self.debug,
            'database_uri': self.database_uri,
            'log_level': self.log_level,
            'port': self.port
        }