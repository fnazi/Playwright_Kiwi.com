# Use official Playwright image with Python
FROM mcr.microsoft.com/playwright/python:v1.42.0-jammy

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install chromium

# Copy all files
COPY . .

# Command to run tests
CMD ["pytest", "-v", "--html=report.html", "--self-contained-html"]