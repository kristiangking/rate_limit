import time
from collections import deque

# Maximum number of requests a customer can make within the interval
MAX_PERMITTED_REQUESTS = 10

# The rolling time window in seconds
INTERVAL = 60


class RateLimiter:
    def __init__(self, max_requests: int = MAX_PERMITTED_REQUESTS, interval: int = INTERVAL):
        # Store the maximum number of requests allowed per interval
        self.max_requests = max_requests

        # Store the length of the rolling window in seconds
        self.interval = interval

        # Initialise an empty dictionary to map each customerId to their request timestamps
        self.customer_requests: dict[int, deque] = {}

    def rateLimit(self, customerId: int) -> bool:
        """
        Returns True if the request is ALLOWED, False if the customer has EXCEEDED the rate limit.
        """
        # Capture the current time in seconds since epoch
        now = time.time()

        # Calculate the earliest timestamp that falls within the rolling window
        window_start = now - self.interval

        # If this customer has no recorded requests yet, create a new empty deque for them
        if customerId not in self.customer_requests:
            self.customer_requests[customerId] = deque()

        # Retrieve the deque of timestamps for this customer
        timestamps = self.customer_requests[customerId]

        # Loop through the oldest timestamps at the front of the deque
        while timestamps and timestamps[0] < window_start:
            # Remove any timestamp that falls outside the rolling window
            timestamps.popleft()

        # Check if the number of requests in the window has already reached the limit
        if len(timestamps) >= self.max_requests:
            # Customer has exceeded the limit — return False to indicate the request is denied
            return False

        # Request is within the limit — record the current timestamp for this customer
        timestamps.append(now)

        # Return True to indicate the request is allowed
        return True
