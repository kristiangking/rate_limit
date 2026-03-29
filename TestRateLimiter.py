limiter = RateLimiter()

customer_a = 101
customer_b = 202

# Simulate 11 rapid requests for customer A
for i in range(11):
    blocked = limiter.rate_limit(customer_a)
    print(f"Request {i+1} for customer {customer_a}: {'BLOCKED' if blocked else 'ALLOWED'}")

# Customer B is unaffected
print(f"\nCustomer {customer_b}: {'BLOCKED' if limiter.rate_limit(customer_b) else 'ALLOWED'}")
