# main.py

import geopandas as gpd
import os
import pathlib # for the path objects

# Import modules
from config import DATABASE_URL, DATA_FILES
from cleaner import clean_data
from db_connector import get_db_engine, load_to_db

if __name__ == "__main__":
    print("Starting Modular ETL Process")

    # Ensures password loaded successfully from environment variable
    if not DATABASE_URL or 'None' in DATABASE_URL:
        print("\nFATAL ERROR: The database password is not set.")
        print("ACTION: Please run the 'export GREENWAY_DB_PASS=\"<your_password>\"' command in your terminal.")
        exit(1)

    # 2. Establishes the database connection
    engine = get_db_engine(DATABASE_URL)

    for table_name, file_path in DATA_FILES.items():
        # Check pathlib Path object exists
        if file_path.exists():
            print(f"\nProcessing file: {file_path}")

            # Extract: Reads the GeoJSON file, converts the Path object to a string for geopandas
            gdf = gpd.read_file(str(file_path), engine='fiona') #Force using Fiona as the engine

            # Transform: Uses external cleaning module
            cleaned_gdf = clean_data(gdf, table_name)

            # Load: Uses external database module to write to PostGIS
            load_to_db(cleaned_gdf, table_name, engine)
        else:
            print(f"File not found: {file_path}. Please ensure ./fetch_data.sh was run successfully.")

    print("\nETL Process Complete.")
