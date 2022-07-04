# Set base image (host OS)
FROM python:3.10

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /ScanGameBackend

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip3 install -r requirements.txt
RUN apt-get install python3-opencv

# Copy the content of the local src directory to the working directory
COPY * .

# Specify the command to run on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]