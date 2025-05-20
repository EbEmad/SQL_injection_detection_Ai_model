#!/bin/bash
# move to the app directory
echo " *************** Runnign app.... **************************** "
# Set default values if env vars aren't provided
RUN_PORT=${RUN_PORT:-5000}
RUN_HOST=${APP_HOST:-0.0.0.0}

# Run the app using Gunicorn with UvicornWorker
gunicorn -k uvicorn.workers.UvicornWorker -b ${RUN_HOST}:${RUN_PORT} app:app
