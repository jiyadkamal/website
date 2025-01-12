# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
RUN pip install --no-cache-dir fastapi uvicorn google-generativeai python-multipart

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "test:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
