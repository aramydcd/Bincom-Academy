# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Postgres driver
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code (to-do.py, _init_.py, etc.)
COPY . .

# Command to run the server
CMD ["python", "main.py"]