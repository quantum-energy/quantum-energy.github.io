# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the desired port (e.g., 5500)
EXPOSE 5500

# Run the Flask app
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5500"]
