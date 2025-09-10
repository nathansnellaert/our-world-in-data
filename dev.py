"""Development script for testing COVID-19 connector"""
import os

# Set environment variables for local development
os.environ['CONNECTOR_NAME'] = 'covid-19'
os.environ['RUN_ID'] = 'local-dev'
os.environ['ENABLE_HTTP_CACHE'] = 'true'
os.environ['CACHE_REQUESTS'] = 'false'
os.environ['DISABLE_STATE'] = 'false'
os.environ['CATALOG_TYPE'] = 'local'
os.environ['DATA_DIR'] = 'data'

# Run the main connector
from main import main

if __name__ == "__main__":
    main()