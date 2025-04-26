# USE THE BASE IMAGE OF PYTHON
FROM  python:latest

# SET THE WORKING DIRECTORY
WORKDIR /app

# COPY THE REQUIREMENTS FILE
COPY reqirements.txt .
COPY ./run.sh .
RUN chmod +x /app/run.sh
# INSTALL THE DEPENDENCIES
RUN pip install --no-cache-dir -r reqirements.txt
WORKDIR /app/scripts

# EXPOSE THE PORT THE APP WILL RUN ON

EXPOSE 5000

# COMMAND TO RUN TEHE APP
CMD ["./run.sh"]
