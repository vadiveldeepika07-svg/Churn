# Use lightweight Python image
#FROM --platform=arm64 python:3.10-slim
FROM --platform=windows/arm64 mcr.microsoft.com/windows/servercore:ltsc2022

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        git \
        curl \
        wget \
        libssl-dev \
        libffi-dev \
        python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt .


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        git \
        curl \
        wget \
        libssl-dev \
        libffi-dev \
        python3-dev \
    || apt-get install -f --fix-missing && \
    rm -rf /var/lib/apt/lists/*





RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and model folder
COPY app /app/app

COPY model/ /app/model/
# Expose port
EXPOSE 8001

# Start FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
