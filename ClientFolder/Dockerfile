# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install core dependencies
#RUN apt-get update \
#    && apt-get install -y libpq-dev build-essential \
#    && rm -rf /var/lib/apt/lists/

# Copy the current directory contents
COPY . .
COPY requirements.txt /app/requirements.txt
COPY server-side.py /app/server-side.py
#COPY input-fd-data.sql /app/input-fd-data.sql
COPY input-tldr-data.sql /app/input-tldr-data.sql

# Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install PostgreSQL
#RUN apt-get update && apt-get install -y postgresql-client

# Copy the entrypoint script into the Docker Image
#COPY entrypoint.sh /app/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose the port the app runs on
EXPOSE 8888

# update permissions
RUN chmod +x client-side.py
RUN chmod +x input-tldr-data.sql

# Run the script
CMD ["python", "client-side.py"]

# Set the entrypoint of the Docker container
ENTRYPOINT ["/app/entrypoint.sh"]
