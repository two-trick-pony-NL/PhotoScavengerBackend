# Set base image (host OS)
FROM python:3.10-buster

# By default, listen on port 5000
EXPOSE 80/tcp

# Set the working directory in the container
WORKDIR /photoscavenger

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY calculateassignment.py .
COPY gunicorn.sh .
COPY ImageDetector.py .
COPY ImageDetectorV1.py .
COPY yolov5m.pt .
COPY ImageDetectorV2.py .
COPY main.py .
COPY newassignmentV1.py .
COPY newassignmentV2.py .
COPY stats.json .
COPY statshistoric.json .
COPY assignments ./assignments
COPY templates ./templates
COPY models ./models
COPY static ./static
COPY Tests ./tests

# Specify the command to run on container start
ENTRYPOINT ["./gunicorn.sh"]
