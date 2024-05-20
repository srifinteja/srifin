import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import sys
sys.path.append('/path/to/directory')
import config

# Define file paths
excel_path = [r"C:\Users\Teja\Downloads\2024-04-29_village.csv",r"C:\Users\Teja\Downloads\2024-05-06_village_Axis.csv"]
geojson_path = r"C:\Users\Teja\Downloads\combined_geojson.geojson"

# Load and concatenate Excel data
df_list = [pd.read_csv(path, encoding='cp1252') for path in excel_path]
df_excel = pd.concat(df_list, ignore_index=True)
# Filter out rows where Latitude or Longitude are 0
df_excel = df_excel[(df_excel['Lattitide'] != 0) & (df_excel['Longitude'] != 0)]
print(df_excel['Lattitide'])
df_excel['Lattitide'] = ''+ df_excel['Lattitide'].astype(str)
print(df_excel['Lattitide'])
print(df_excel['Lattitide'].dtype)
df_excel['Lattitide'] = df_excel['Lattitide'].astype(str)
df_excel['Longitude'] = df_excel['Longitude'].astype(str)
# df_excel['Lattitide'] = df_excel['Lattitide'].astype(str) 
print(df_excel['Lattitide'].dtype)
# Filter rows where 'Latitude' column contains non-numeric values
non_numeric_latitude = df_excel[pd.to_numeric(df_excel['Lattitide'], errors='coerce').isna()]

# Print non-numeric values in 'Latitude' column
print("Non-numeric values in 'Latitude' column:")
print(non_numeric_latitude['Lattitide'])

# Load GeoJSON data
gdf_geojson = gpd.read_file(geojson_path)

# Ensure the GeoDataFrame has the correct coordinate reference system
gdf_geojson = gdf_geojson.set_crs("EPSG:4326")

# Create a GeoDataFrame from Excel data
# Note: Make sure to use the correct column names for latitude and longitude as they appear in your CSV
gdf_excel = gpd.GeoDataFrame(
    df_excel, 
    geometry=gpd.points_from_xy(df_excel.Longitude, df_excel.Lattitide),
    crs="EPSG:4326"
)

# Initialize columns in gdf_excel for the GeoJSON properties
geojson_props = ["Village", "Pincode", "Remarks", "district", "state", "tot_p_2011", "no_hh_2011", "censuscode2011"]
for prop in geojson_props:
    gdf_excel[prop] = None

# Spatial join to find which points from Excel fall within the GeoJSON polygons
gdf_joined = gpd.sjoin(gdf_excel, gdf_geojson, predicate='intersects')
unmatched_rows = gdf_excel[~gdf_excel.index.isin(gdf_joined.index)]

# Check if there are any unmatched rows, and print them
if not unmatched_rows.empty:
    # output_unmatched_path = r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\village_not_found.xlsx"
    output_unmatched_path = f"{config.folder_path}\\village_not_found.xlsx"
    unmatched_rows.drop(columns=["geometry"]).to_excel(output_unmatched_path, index=False)
    print(f"Rows with no matching village details in the GeoJSON file were written to: {output_unmatched_path}",flush=True)
else:
    print("All rows matched with village details in the GeoJSON file.",flush=True)

# Save the merged data to a new Excel file
# output_excel_path = r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_Latest.xlsx"
output_excel_path = f"{config.folder_path}\\Village_detail_Latest.xlsx"
# output_path = f"{config.folder_path}\\villages\\{village}_Source_Map.xlsx"
gdf_joined.drop(columns=["index_right", "geometry"]).to_excel(output_excel_path, index=False)

print("Merging completed. The output is saved to:", output_excel_path,flush=True)

