# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python packages
RUN pip install confluent-kafka

# Run the consumer script when the container launches
CMD ["python", "-u","kafka_consumer_demo.py"]
