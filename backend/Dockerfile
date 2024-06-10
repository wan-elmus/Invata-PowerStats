
# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install pip dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -U pip3 && pip3 install -r requirements.txt

# Copy project files into the container
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
