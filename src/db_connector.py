# db_connector.py

from sqlalchemy import create_engine

def get_db_engine(database_url):
    """Creates/returns the SQLAlchemy engine"""
    return create_engine(database_url)

def load_to_db(df, table_name, engine):
    """Loads GeoDataFrame into PostgreSQL/PostGIS"""
    print(f"Loading {table_name} into PostgreSQL...")
    
    # Uses GeoPandas' built-in to_postgis method for geospatial data
    try:
        df.to_postgis(
            name=table_name,
            con=engine,
            if_exists='replace', 
            index=False
        )
        print(f"SUCCESS: Data loaded into table: {table_name}")
    except Exception as e:
        print(f"ERROR loading {table_name}: {e}")
