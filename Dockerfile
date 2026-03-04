# Lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies first (better for Docker caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose port 5000
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]