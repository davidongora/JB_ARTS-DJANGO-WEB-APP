# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev-compat \
    libmariadb-dev \
    gcc \
    python3-dev \
    postgresql \
    postgresql-contrib \
    libpq-dev \
    && apt-get clean


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the entire project into the working directory
COPY . /app/

# Expose the port Django will run on
EXPOSE 8000

# Run migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Start the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
