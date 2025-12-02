# cleaner.py

def clean_data(df, table_name):
    """
    Cleans column names
    and ensures compatibility with PostGIS.
    """
    print(f"Cleaning {table_name} data...")
    # Converts column names to lowercase, replaces spaces with underscores 
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    
    # Ensures the geometry column is named 'geom' (PostGIS compatibility)
    if df.geometry.name != 'geom':
        df = df.rename_geometry('geom')
        
    return df
