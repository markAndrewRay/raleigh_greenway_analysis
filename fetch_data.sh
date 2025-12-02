#!/bin/bash
# Script: fetch_data.sh
# Purpose: Downloads raw data from Raleigh's data portal.

echo "Starting Data Acquisition"

#1. Greenways (Lines)
GREENWAYS_URL="https://opendata.arcgis.com/datasets/2849887754b248a39a7d97609a32128a_0.geojson"
echo "Downloading Greenway Segments..."
# -sL flags tell curl to be silent and follow redirects
curl -sL "$GREENWAYS_URL" -o raw_data/greenways.geojson

#2. Amenities/Facilities (Points)
AMENITIES_URL="https://opendata.arcgis.com/datasets/7710b7543166415a9757f59737150a00_0.geojson"
echo "Downloading Amenity Locations..."
curl -sL "$AMENITIES_URL" -o raw_data/amenities.geojson

echo "Acquisition Complete."
