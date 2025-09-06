"""Fetch and process COVID-19 data from Our World in Data"""
import pyarrow as pa
from utils.http_client import get
from utils.io import load_state, save_state
from datetime import datetime, timezone

DATA_SOURCE_URL = 'https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.csv'

def fetch_covid_data():
    """Fetch COVID-19 data from Our World in Data"""
    response = get(DATA_SOURCE_URL)
    response.raise_for_status()
    return response.text

def process_covid_data():
    """Process COVID-19 data"""
    import pandas as pd
    from io import StringIO
    
    # Load state
    state = load_state("covid_data")
    
    # Fetch data
    csv_data = fetch_covid_data()
    df = pd.read_csv(StringIO(csv_data))
    
    # Convert date to proper format
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    
    # Select relevant columns and drop nulls
    df = df[['date', 'location', 'iso_code', 'new_cases', 'new_deaths']].dropna()
    
    # Convert to PyArrow table
    table = pa.Table.from_pandas(df, preserve_index=False)
    
    # Update state
    save_state("covid_data", {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "row_count": len(table)
    })
    
    return table