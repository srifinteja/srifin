import pandas as pd
import geopandas as gpd
import os
import sys
sys.path.append('/path/to/directory')
import config
from shapely.geometry import Point, shape

# Define file paths
output_folder = config.folder_path
excel_path = [
    r"C:\Users\Teja\Downloads\2024-04-29_center.csv",
    r"C:\Users\Teja\Downloads\2024-05-06_center_Axis.csv"
]
geojson_path = r"C:\Users\Teja\Downloads\combined_geojson.geojson"

# Load and concatenate Excel data
df_list = [pd.read_csv(path, encoding='ISO-8859-1') for path in excel_path]
df_excel = pd.concat(df_list, ignore_index=True)
# Define the output path for the Excel file
output_excel_path = os.path.join(output_folder, 'Combined_Data.xlsx')

# Save the DataFrame to an Excel file
df_excel.to_excel(output_excel_path, index=False)  # Set index=False to not include row indices in the file

print(f'Data saved to Excel file at: {output_excel_path}')
# Convert the 'location_long' and 'location_lat' columns to float, coercing errors
df_excel['location_long'] = pd.to_numeric(df_excel['location_long'], errors='coerce')
df_excel['location_lat'] = pd.to_numeric(df_excel['location_lat'], errors='coerce')

# Optionally, drop rows with NaN values in these columns if they're essential
df_excel = df_excel.dropna(subset=['location_long', 'location_lat'])

# Convert the entire 'center_name' column to string and clean it
df_excel['center_name'] = df_excel['center_name'].astype(str)
df_excel['center_name'] = df_excel['center_name'].apply(lambda x: x[1:] if x.startswith('=') else x)

# Load GeoJSON data and ensure the GeoDataFrame has the correct coordinate reference system
gdf_geojson = gpd.read_file(geojson_path).set_crs("EPSG:4326")

# Create a GeoDataFrame from Excel data
gdf_excel = gpd.GeoDataFrame(df_excel, geometry=gpd.points_from_xy(df_excel.location_long, df_excel.location_lat), crs="EPSG:4326")

# Initialize columns in gdf_excel for the GeoJSON properties
geojson_props = ["Village", "Pincode", "Remarks", "district", "state", "tot_p_2011", "no_hh_2011", "censuscode2011"]
for prop in geojson_props:
    gdf_excel[prop] = None

# Spatial join to find which points from Excel fall within the GeoJSON polygons
gdf_joined = gpd.sjoin(gdf_excel, gdf_geojson, predicate='intersects')
unmatched_rows = gdf_excel[~gdf_excel.index.isin(gdf_joined.index)]

# Handle unmatched rows
if not unmatched_rows.empty:
    output_unmatched_path = os.path.join(output_folder, "Center_not_found.xlsx")
    unmatched_rows.drop(columns=["geometry"]).to_excel(output_unmatched_path, index=False)
    print(f"Rows with no matching village details in the GeoJSON file were written to: {output_unmatched_path}")
else:
    print("All rows matched with village details in the GeoJSON file.")

# Save the merged data to a new Excel file
output_excel_path = os.path.join(output_folder, "center_detail_Latest.xlsx")
gdf_joined.drop(columns=["index_right", "geometry"]).to_excel(output_excel_path, index=False)

print("Merging completed. The output is saved to:", output_excel_path)
