# Use a Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Create static/uploads and db directories
RUN mkdir -p static/uploads db

# Expose the port (CataractSense uses 8001)
EXPOSE 8001

# Command to run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]