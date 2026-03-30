from RateLimiter import RateLimiter

limiter = RateLimiter()

customer_a = 101
customer_b = 202

# Simulate 11 rapid requests for customer A
for i in range(20):
    blocked = limiter.rateLimit(customer_a)
    print(f"Request {i+1} for customer {customer_a}: {'ALLOWED' if blocked else 'BLOCKED'}")

# Customer B is unaffected
print(f"\nCustomer {customer_b}: {'ALLOWED' if limiter.rateLimit(customer_b) else 'BLOCKED'}")
