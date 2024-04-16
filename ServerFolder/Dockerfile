# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install core dependencies
#RUN apt-get update \
#    && apt-get install -y libpq-dev build-essential \
#    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file separately to leverage Docker layer caching
COPY requirements.txt .

# Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt --verbose

# Copy the rest of the application code
COPY . .

# Update permissions for executable scripts
RUN chmod +x server-side.py

# Expose the port the app runs on
EXPOSE 8888

# Run the script
CMD ["python", "server-side.py"]