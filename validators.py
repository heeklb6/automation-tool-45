import re

def is_valid_email(email: str) -> bool:
    """Check if the email address is valid."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


def is_positive_integer(value: int) -> bool:
    """Check if the value is a positive integer."""
    return isinstance(value, int) and value > 0


def is_non_empty_string(value: str) -> bool:
    """Check if the string is non-empty."""
    return isinstance(value, str) and len(value) > 0


def is_valid_url(url: str) -> bool:
    """Check if the URL is valid."""
    url_regex = r'^(https?://)?(www\.)?([a-zA-Z0-9-]+\.[a-zA-Z]{2,}|localhost)(:[0-9]{1,5})?(/.*)?$'
    return re.match(url_regex, url) is not None


def is_in_range(value: int, min_value: int, max_value: int) -> bool:
    """Check if the value is within a specified range."""
    return isinstance(value, int) and min_value <= value <= max_value
