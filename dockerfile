# USE THE BASE IMAGE OF PYTHON
FROM python:3.11-slim

# SET THE WORKING DIRECTORY
WORKDIR /app

# COPY THE REQUIREMENTS FILE
COPY reqirements.txt .
# INSTALL THE DEPENDENCIES
RUN pip install --no-cache-dir -r reqirements.txt
COPY run.sh /app/run.sh
RUN chmod +x run.sh
# COPY THE SOURCE CODE
COPY . .
# EXPOSE THE PORT THE APP WILL RUN ON
EXPOSE 5000

# COMMAND TO RUN TEHE APP
CMD [ "bash","run.sh" ]
