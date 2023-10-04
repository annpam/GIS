import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import os

# Read csv
df = pd.read_csv('Modern Ethnic.csv')

# Create a GeoDataFrame from the DataFrame by adding a geometry column with Point objects
geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]

# Create the GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# Define the coordinate reference system (CRS)
gdf.crs = 'EPSG:4326'

# Save the result as shapefile
output_shapefile_path = r'H:\My Drive\Freelance\Porto\Python\output.shp'
gdf.to_file(output_shapefile_path)