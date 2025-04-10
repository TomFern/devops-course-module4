from prometheus_client import start_http_server, Summary
import random
import time

# Create a metric to track time spent processing a request.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def process_request(t):
    time.sleep(t)

if __name__ == '__main__':
    # Start up the Prometheus metrics server on port 8000
    start_http_server(8000)
    # Generate some requests continuously.
    while True:
        process_request(random.random())

