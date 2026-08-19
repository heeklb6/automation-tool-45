class CryptoError(Exception):
    """Base class for all custom exceptions in the crypto module."""
    pass

class NetworkError(CryptoError):
    """Exception raised for network-related errors."""
    def __init__(self, message):
        super().__init__(message)

class ValidationError(CryptoError):
    """Exception raised for validation errors of input data."""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f'Validation error in {field}: {message}')

class ConfigurationError(CryptoError):
    """Exception raised for configuration-related errors."""
    def __init__(self, message):
        super().__init__(message)