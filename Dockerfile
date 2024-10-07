# Start from an official Python image that already has common dependencies
FROM python:3.10-bullseye

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential git curl

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port and run the app
EXPOSE 8000

CMD ["python", "others/del.py"]
