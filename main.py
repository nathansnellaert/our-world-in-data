"""Our World in Data Connector"""
import os
os.environ['CONNECTOR_NAME'] = 'our-world-in-data'
os.environ['RUN_ID'] = os.getenv('RUN_ID', 'local-run')

from utils import validate_environment, upload_data
from assets.covid_data.covid_data import process_covid_data

def main():
    validate_environment()
    
    # Process COVID-19 data
    covid_data = process_covid_data()
    
    # Upload dataset
    upload_data(covid_data, "covid_19_cases_deaths")


if __name__ == "__main__":
    main()