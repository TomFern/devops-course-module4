FROM python:3.12-bookworm

# Create a non-root user and group
RUN addgroup --system appgroup && adduser --system --group appuser

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

# Copy the application code and change ownership
COPY . .
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

EXPOSE 4000

CMD ["python", "app.py"]

