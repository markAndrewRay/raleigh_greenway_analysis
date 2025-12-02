# config.py
import os
import pathlib # for reliable path resolution

# Defines the absolute path to the project root directory
PROJECT_ROOT = pathlib.Path(__file__).parent.parent 

# DATABASE CREDENTIALS
# Loads the password from the OS environment variable (security)
DB_PASSWORD = os.environ.get('GREENWAY_DB_PASS') 
DB_USER = 'greenway_admin'
DB_NAME = 'greenway_db'
DB_HOST = 'localhost' 
DB_PORT = '5432'

# FILE PATHS
DATA_FILES = {
    # join the project root path with the relative raw_data folder
    'greenways': PROJECT_ROOT / 'raw_data/greenways.geojson',
    'amenities': PROJECT_ROOT / 'raw_data/amenities.geojson'
}

# DATABASE URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
