import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config
# "C:\Users\Teja\Downloads\Combined_Village_Boundary_2023.csv"
# Paths to the CSV files
csv_file_paths = [
    r"C:\Users\Teja\Downloads\Combined_Village_Boundary_2023.csv"
    # r"C:\Users\Vijval\Downloads\KA_Village_Boundary_2023.csv",
    # r"C:\Users\Vijval\Downloads\BR_Village_Boundary_2023.csv",
]
# "C:\Users\Teja\Downloads\Vijval\output_with_track_status.xlsx"
# Load the Village_Details.xlsx file
# village_details_path = r"C:\Users\Teja\Downloads\Vijval\output_with_track_status.xlsx"
village_details_path = f"{config.folder_path}\\output_with_track_status.xlsx"
village_details_df = pd.read_excel(village_details_path, dtype={'censuscode2011': str})
# print(village_details_df['censuscode2011_right'].head())
# Initialize an empty dictionary for the censuscode2011 to tru_2011 mapping
census_to_tru_mapping = {}

# Loop through each CSV file path
for csv_file_path in csv_file_paths:
    # Load the current CSV file
    boundary_df = pd.read_csv(csv_file_path, dtype={'censuscode2011': str})
    # Convert and clean up the censuscode2011_right column
    boundary_df['censuscode2011'] = boundary_df['censuscode2011'].astype(str).str.split('.').str[0]
    # print(boundary_df['censuscode2011'].head())
    # Update the mapping dictionary with the current CSV's data
    # This assumes tru_2011 values are the same for any repeated censuscode2011 across files
    # If they might differ, you'll need to decide how to handle the discrepancies
    census_to_tru_mapping.update(boundary_df.set_index('censuscode2011')['tru_2011'].to_dict())

# Check for unmatched census codes (optional, can be removed to speed up the process)
unmatched_codes = set(village_details_df['censuscode2011']) - set(census_to_tru_mapping.keys())
# if unmatched_codes:
    # print(f"Unmatched census codes: {unmatched_codes}")

# Map the 'tru_2011' values to the village details DataFrame using the 'censuscode2011' column
village_details_df['tru_2011'] = village_details_df['censuscode2011'].map(census_to_tru_mapping)

# Handle rows with missing 'tru_2011' data by setting a default value
village_details_df['tru_2011'] = village_details_df['tru_2011'].fillna('Missing')
# Remove the "Remark" column from the DataFrame if it exists
if 'Remarks' in village_details_df.columns:
    village_details_df = village_details_df.drop(columns=['Remarks'])

# Save the updated DataFrame back to the Excel file
village_details_df.to_excel(village_details_path, index=False, engine='openpyxl')

print(f"The Village_Details.xlsx file has been updated with tru_2011 data.")
