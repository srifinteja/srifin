import os
import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config
# # Set the current working directory to the script's directory
# script_dir = os.path.dirname(os.path.abspath(__file__))
# os.chdir(script_dir)


## get tru2011 from Combined_Village_Boundary_2023 and add it to Village_detail_Latest with primanry key censuscode2011

# Paths to the CSV files
csv_file_paths = [
    r"C:\Users\Teja\Downloads\Combined_Village_Boundary_2023.csv"
    # Uncomment and add more paths as needed
    # r"C:\Users\Vijval\Downloads\KA_Village_Boundary_2023.csv",
    # r"C:\Users\Vijval\Downloads\BR_Village_Boundary_2023.csv",
]

# # Create the output directory if it doesn't exist
# output_dir = os.path.join(script_dir, "outputs")
# os.makedirs(output_dir, exist_ok=True)

# Load the Village_Details.xlsx file from the outputs directory
# village_details_path = os.path.join(output_dir, "Village_detail_Latest.xlsx")
# C:\Users\Teja\Desktop\Karthik\demo\py_outputs\
# village_details_path = "C:\\Users\\Teja\\Desktop\\Karthik\\demo\\py_outputs\\Village_detail_Latest.xlsx"
# village_details_path = config.folder_path + "\\Village_detail_Latest.xlsx"
village_details_path = f"{config.folder_path}\\Village_detail_Latest.xlsx"
village_details_df = pd.read_excel(village_details_path, dtype={'censuscode2011_right': str})

# Initialize an empty dictionary for the censuscode2011 to tru_2011 mapping
census_to_tru_mapping = {}

# Loop through each CSV file path
for csv_file_path in csv_file_paths:
    # Load the current CSV file
    boundary_df = pd.read_csv(csv_file_path, dtype={'censuscode2011': str})
    # Clean up the censuscode2011 column
    boundary_df['censuscode2011'] = boundary_df['censuscode2011'].astype(str).str.split('.').str[0]
    
    # Update the mapping dictionary with the current CSV's data
    census_to_tru_mapping.update(boundary_df.set_index('censuscode2011')['tru_2011'].to_dict())

# Map the 'tru_2011' values to the village details DataFrame using the 'censuscode2011' column
village_details_df['tru_2011'] = village_details_df['censuscode2011_right'].map(census_to_tru_mapping)

# Handle rows with missing 'tru_2011' data by setting a default value
village_details_df['tru_2011'] = village_details_df['tru_2011'].fillna('Missing')

# Remove the "Remark" column from the DataFrame if it exists
if 'Remarks' in village_details_df.columns:
    village_details_df = village_details_df.drop(columns=['Remarks'])

# Save the updated DataFrame back to the Excel file in the outputs directory
village_details_df.to_excel(village_details_path, index=False, engine='openpyxl')

print(f"The Village_Detail_Latest.xlsx file has been updated with tru_2011 data and saved in the 'outputs' directory.")
