FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install the Prometheus client library
RUN pip install --no-cache-dir prometheus_client

# Copy the metrics application code into the container
COPY metrics_app.py .

# Expose port 8000, which the app uses to serve metrics
EXPOSE 8000

# Define the command to run the metrics app
CMD ["python", "metrics_app.py"]

