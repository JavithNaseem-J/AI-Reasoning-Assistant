from prometheus_client import Counter, Histogram

# Define Prometheus metrics
REQUEST_COUNT = Counter("reasoning_requests_total", "Total reasoning requests")
LATENCY = Histogram("reasoning_latency_seconds", "Request latency in seconds")

def log_request_start():
    REQUEST_COUNT.inc()

def log_request_latency(duration: float):
    LATENCY.observe(duration)
