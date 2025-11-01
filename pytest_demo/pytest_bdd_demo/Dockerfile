# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set a working directory inside the container
WORKDIR /app/pytest_bdd_demo

# Copy requirements first (for Docker layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code into the container
COPY . .

# Default command: run pytest when the container starts
CMD ["pytest", "-v"]