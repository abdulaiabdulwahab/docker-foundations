# Start from an existing Python image
FROM python:3.13-slim


# Set the working directory inside the image
WORKDIR /app


# Copy dependency definition first.
# This improves Docker build caching.
COPY requirements.txt .


# Install Python dependencies inside the image
RUN pip install --no-cache-dir -r requirements.txt


# Copy our application into the image
COPY app.py .


# Document the port the application uses
EXPOSE 5000


# Command executed when a container starts
CMD ["python", "app.py"]