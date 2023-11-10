import time

class RateLimiter:
    def __init__(self, max_requests, time_interval):
        self.max_requests = max_requests
        self.time_interval = time_interval
        self.tokens = max_requests
        self.last_refill_time = time.time()

    def _refill_tokens(self):
        current_time = time.time()
        time_passed = current_time - self.last_refill_time
        tokens_to_add = time_passed / self.time_interval
        self.tokens = min(self.max_requests, self.tokens + tokens_to_add)
        self.last_refill_time = current_time

    def check_request(self):
        self._refill_tokens()
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False

# Example usage
