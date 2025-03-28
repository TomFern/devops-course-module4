# Use an official Python runtime as a base image.
FROM python:3.9-slim

# Environment variables to ensure proper Python behavior.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container.
WORKDIR /app

# Copy the requirements file and install dependencies.
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code.
COPY . /app/

# Expose the port the app runs on.
EXPOSE 4000

# Define the command to run the app.
CMD ["python", "app.py"]

