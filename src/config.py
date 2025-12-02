# config.py
import os

# DB CREDENTIALS 
# loads the password from the OS environment variable for security
DB_PASSWORD = os.environ.get('GREENWAY_DB_PASS') 
DB_USER = 'greenway_admin'
DB_NAME = 'greenway_db'
DB_HOST = 'localhost' 
DB_PORT = '5432'

# PATHS
DATA_FILES = {
    'greenways': 'raw_data/greenways.geojson',
    'amenities': 'raw_data/amenities.geojson'
}

# DATABASE URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# TESTING BLOCK 
if __name__ == "__main__":
    print("\nCONFIGURATION TEST")
    if DB_PASSWORD and 'None' not in DATABASE_URL:
        # Mask the password for secure display
        masked_url = DATABASE_URL.replace(DB_PASSWORD, '********')
        print(f"SUCCESS: Database URL configured.")
        print(f"URL: {masked_url}")
    else:
        print("FAILURE: DB_PASSWORD is missing!")
        print("ACTION: Run 'export GREENWAY_DB_PASS=\"<your_password>\"' in your terminal.")
    print("--------------------------")
