Greenway Restroom Accessibility Analysis

This project analyzes the accessibility of existing restroom facilities along the Raleigh Greenways network using spatial buffer and intersection analysis. The goal is to determine what percentage of the network is within a comfortable walking distance (750m radius) of an amenity for long-distance users (e.g., Nordic walkers).

System & Environmental Dependencies

This project is built using Python for the geospatial analysis and relies on a PostgreSQL/PostGIS backend. All dependencies are managed via a reproducible Mamba environment.

1. System-Level Dependencies

The operating system requires the following prerequisite software:

    Dependency: Python

        Purpose: Core Programming Language

        Requirement: Version 3.10 or higher

    Dependency: Mamba

        Purpose: Environment & Package Manager

        Requirement: Latest version recommended

    Dependency: Git

        Purpose: Version Control

        Requirement: Latest version recommended

    Dependency: PostgreSQL

        Purpose: Open-source relational database.

        Requirement: Latest stable version

    Dependency: PostGIS

        Purpose: Spatial extension for PostgreSQL.

        Requirement: Latest stable version


2. Environmental Dependencies (Python Packages)

All required Python packages are listed in the environment.yml file.

    Package: geopandas

        Purpose: Core library for spatial data manipulation (buffer, intersection, export).

    Package: sqlalchemy

        Purpose: Python SQL Toolkit (Used to build the DB connection URL).

    Package: psycopg2

        Purpose: PostgreSQL adapter for Python (Used for connecting to PostGIS).

    Package: matplotlib

        Purpose: Plotting library for basic in-notebook map visualization.

    Package: tabulate

        Purpose: Used by Pandas to render clean Markdown tables for KPI summary.

3. Setting Up the Environment

	A. PostGIS Database Setup

		Start the PostgreSQL Server: Before proceeding, ensure your PostgreSQL service is running. This command depends on your OS and installation method:

			macOS/Linux Example (Service): pg_ctl -D /usr/local/var/postgres start

        		Windows Example (Services Manager): Open the Windows Services application (Run services.msc), find your PostgreSQL service (e.g., postgresql-x64-16), and click Start.

    		Access the SQL Shell and Create User/Database: You must now enter the SQL command line interface (psql) to set up the user and database structure.

        		macOS/Linux: Run psql -U postgres directly in the terminal.

        		Windows: Navigate to the bin directory of your PostgreSQL installation first (e.g., cd "C:\Program Files\PostgreSQL\16\bin"), then run .\psql -U postgres.

    		Once you see the postgres=# prompt, run the following SQL commands sequentially:

    		1. Create a dedicated user for this project
    			CREATE USER greenway_user WITH PASSWORD 'YourSecurePasswordHere'; #(Replace 'YourSecurePasswordHere' with a strong password.)

    		2. Create the project database
    			CREATE DATABASE greenway_db OWNER greenway_user;

    		3. Connect to the new database
    			\c greenway_db greenway_user

    		4. Enable PostGIS extension
    			CREATE EXTENSION postgis;

    		5. Quit the psql shell
    			\q
    
	B. Python Environment Setup

    		Clone the Repository:

    			git clone https://github.com/markAndrewRay/raleigh_greenway_analysis.git
    			cd raleigh_greenway

    		Create and Activate the Mamba/Conda Environment:

    			mamba env create -f environment.yml
    			mamba activate geo_env_hybrid

4. Credential Management & Notebook Execution

This project connects to the PostGIS database securely by reading credentials directly from System Environment Variables (via Python's os.environ). DO NOT hardcode your passwords into the notebook code or commit them to Git.

	Execution Instructions

    		Stop the Notebook and Deactivate the Environment (if already active).

    		Initialize Credentials in Terminal: You must set the following four environment variables in your terminal session before launching the notebook. Substitute the values in brackets ([...]) with your actual PostGIS credentials.

    			Variable Name: POSTGRES_USER

        			Purpose: Database username (greenway_user from setup step)

        			Command (Linux/macOS - Bash/Zsh): export POSTGRES_USER='[your_user]'

        			Command (Windows - PowerShell): $env:POSTGRES_USER='[your_user]'

    			Variable Name: POSTGRES_PASS

        			Purpose: Database Password (The password used in the CREATE USER command)

        			Command (Linux/macOS - Bash/Zsh): export POSTGRES_PASS='[YOUR_PASSWORD]'

        			Command (Windows - PowerShell): $env:POSTGRES_PASS='[YOUR_PASSWORD]'

    			Variable Name: POSTGRES_HOST

        			Purpose: Database host (e.g., localhost)

        			Command (Linux/macOS - Bash/Zsh): export POSTGRES_HOST='localhost'

        			Command (Windows - PowerShell): $env:POSTGRES_HOST='localhost'

    			Variable Name: POSTGRES_DB

        			Purpose: Database name (greenway_db)

        			Command (Linux/macOS - Bash/Zsh): export POSTGRES_DB='greenway_db'

        			Command (Windows - PowerShell): $env:POSTGRES_DB='greenway_db'

    				
			Example (Linux/macOS):

    				export POSTGRES_USER='greenway_user'
    				export POSTGRES_PASS='MySecure@P4ss'
    				export POSTGRES_HOST='localhost'
    				export POSTGRES_DB='greenway_db'

    			Example (Windows/PowerShell):

    				$env:POSTGRES_USER='greenway_user'
    				$env:POSTGRES_PASS='MySecure@P4ss'
    				$env:POSTGRES_HOST='localhost'
    				$env:POSTGRES_DB='greenway_db'

		Launch Notebook: (Ensure your geo_env_hybrid is active in the current terminal session.)

    			jupyter lab 01_greenway_exploratory_analysis.ipynb

	The notebook code will now securely retrieve these initialized values to construct the database connection URL.

5. Project Data & Files

	Data Source

    		Original Data: Raleigh GIS Open Data Portal (Greenways layer and amenity data).

6. Key Output Files

	These files are generated by the analysis and are the foundation for the final presentation in Tableau and ArcGIS Pro:

    		File Name: accessibility_kpi_summary.csv

        		Format: CSV

        		Purpose: Input for Tableau. Contains 500m, 750m, and 1000m sensitivity analysis results.

    		File Name: greenway_accessibility_lines_750m.geojson

        		Format: GeoJSON

        		Purpose: Input for ArcGIS Pro/QGIS. Lines color-coded by Accessible/Inaccessible.

    		File Name: restroom_locations.geojson

        		Format: GeoJSON

        		Purpose: Input for ArcGIS Pro/QGIS. Point features of the service locations.
