#!/bin/bash
# Script: fetch_data.sh
# Purpose: Downloads raw data from Raleigh's data portal.

echo "Starting Data Acquisition"

# 1. Greenways (Lines)
GREENWAYS_URL="https://services.arcgis.com/v400IkDOw1ad7Yad/arcgis/rest/services/Greenway_Trails_All/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=geojson"
echo "Downloading Greenway Segments..."
# -sL flags tell curl to be silent and follow redirects
curl -sL "$GREENWAYS_URL" -o raw_data/greenways.geojson

# 2. Amenities/Facilities (Points)
AMENITIES_URL="https://hub.arcgis.com/api/v3/datasets/386697313673498697f476d5cf92c6eb_0/downloads/data?format=geojson&spatialRefId=4326&where=1%3D1"
echo "Downloading Amenity Locations..."
curl -sL "$AMENITIES_URL" -o raw_data/amenities.geojson

echo "Acquisition Complete."
