# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /Projects

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Set the entrypoint command to run the Python application
CMD ["python", "ClothingSimilarity.py"]
