FROM python:3.11-bookworm

WORKDIR /app

# Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# System Requirements
RUN apt update
RUN apt -y upgrade
RUN apt install -y redis-server

# Copy Source Tree
COPY . .

# Rebuild Database
RUN python manage.py flush --noinput
RUN python manage.py migrate

# Set up server
EXPOSE 8000
CMD ["bash", "start_app_docker.sh"]