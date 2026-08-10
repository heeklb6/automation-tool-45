def validate_email(email):
    import re
    if not isinstance(email, str):
        raise ValueError('Email must be a string')
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise ValueError('Invalid email format')
    return True

def validate_age(age):
    if not isinstance(age, int):
        raise ValueError('Age must be an integer')
    if age < 0:
        raise ValueError('Age cannot be negative')
    return True

def validate_username(username):
    if not isinstance(username, str):
        raise ValueError('Username must be a string')
    if not (3 <= len(username) <= 30):
        raise ValueError('Username must be between 3 and 30 characters long')
    if not username.isalnum():
        raise ValueError('Username must only contain letters and numbers')
    return True

# Example usage (to be used during testing):
if __name__ == '__main__':
    try:
        validate_email('test@example.com')
        validate_age(25)
        validate_username('user123')
        print('All validations passed')
    except ValueError as e:
        print(e)