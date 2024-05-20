import pandas as pd
import re
import os

def clean_sheet_name_for_excel(sheet_name):
    """
    Remove or replace invalid characters in sheet names.
    """
    invalid_chars = r'[:\\/?*\[\]]'  # Regex pattern for invalid Excel sheet characters
    clean_name = re.sub(invalid_chars, '_', sheet_name)  # Replace invalid characters with '_'
    return clean_name
# List of full paths to your Excel files
excel_file_paths = [
    r"C:\Users\Vijval\Desktop\codes\Center_UP_East.xlsx",
    r"C:\Users\Vijval\Desktop\codes\Center_UP_West.xlsx",
    r"C:\Users\Vijval\Desktop\codes\Village_UP_East.xlsx",
    r"C:\Users\Vijval\Desktop\codes\Village_UP_West.xlsx",
    r"C:\Users\Vijval\Desktop\codes\Center_Bihar_hits.xlsx",
    r"C:\Users\Vijval\Desktop\codes\Village_Bihar_hits.xlsx",
    r"C:\Users\Vijval\Desktop\codes\Center_Karnataka_hits.xlsx",
    r"C:\Users\Vijval\Desktop\codes\Village_Karnataka_hits.xlsx"
    # Add more paths as needed
]

# Output Excel file name
output_excel_file = 'State_final_Srifin_28th.xlsx'

# Create a Pandas Excel writer using openpyxl as the engine
writer = pd.ExcelWriter(output_excel_file, engine='openpyxl')

# Iterate through the list of file paths
for file_path in excel_file_paths:
    # Read the Excel file
    df = pd.read_excel(file_path)
    # Extract file name without extension for the sheet name
    sheet_name = os.path.splitext(os.path.basename(file_path))[0]
    # Clean the sheet name to remove or replace invalid characters
    clean_name = clean_sheet_name_for_excel(sheet_name)  # Avoid naming conflict
    # Write the dataframe to a sheet with the cleaned sheet name
    df.to_excel(writer, sheet_name=clean_name, index=False)

# Proper method to save the workbook
writer.close() 