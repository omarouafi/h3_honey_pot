# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the new ports that Flask will run on
EXPOSE 5002 5003

# Set environment variable to disable Python output buffering
ENV PYTHONUNBUFFERED=1

# Run both Flask applications (login.py and fakeLogin.py) in the background on the new ports
CMD ["sh", "-c", "python login.py & python fakeLogin.py"]
