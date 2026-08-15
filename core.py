import time
import functools

class RateLimiter:
    """Decorator to limit the rate of function calls."""
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = 0
        self.start_time = time.time()

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.calls >= self.max_calls:
                elapsed = time.time() - self.start_time
                if elapsed < self.period:
                    time.sleep(self.period - elapsed)
                self.calls = 0
                self.start_time = time.time()
            self.calls += 1
            return func(*args, **kwargs)
        return wrapper

@RateLimiter(max_calls=5, period=10)
def fetch_data(api_endpoint):
    # Simulate an API call
    print(f'Fetching data from {api_endpoint}')
    return {'data': 'sample data'}

if __name__ == '__main__':
    for _ in range(20):
        fetch_data('https://api.example.com/data')
        time.sleep(1)