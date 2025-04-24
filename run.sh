#!/bin/bash

# Activate virtual environment (optional in Docker unless you manually created one)
source /opt/venv/vin/activate

# Move to the app directory
cd /app

# Set default values if env vars aren't provided
RUN_PORT=${RUN_PORT:-5000}
RUN_HOST=${HOST:-0.0.0.0}

# Run the app using Gunicorn with UvicornWorker
gunicorn -k uvicorn.workers.UvicornWorker -b $RUN_HOST:$RUN_PORT app:app
