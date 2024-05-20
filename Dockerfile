FROM python:3.8-slim-buster

# Update and install dependencies
RUN apt-get update -y && \
    apt-get install -y awscli

# Set working directory
WORKDIR /app

# Copy all files to the working directory
COPY . /app

# Upgrade pip to the latest version to ensure better handling of large packages
RUN pip install --upgrade pip

# Install dependencies from requirements.txt with a higher timeout
RUN pip install --default-timeout=1000 -r requirements.txt

# Upgrade accelerate package with retry mechanism
RUN for i in 1 2 3; do pip install --upgrade accelerate && break || sleep 30; done

# Set the command to run the application
CMD ["python3", "app.py"]
