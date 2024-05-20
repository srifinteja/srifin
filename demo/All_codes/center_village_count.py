import pandas as pd
from openpyxl import load_workbook
import sys
sys.path.append('/path/to/directory')
import config
# Load the Excel file
# file_path = r"C:\Users\Teja\Downloads\Vijval\Center_detail_latest4.xlsx"
file_path= f"{config.folder_path}\\Center_detail_latest4.xlsx"
df = pd.read_excel(file_path)

branch_villages = {}

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    if pd.notna(row['rec_branch']):
        branches = [branch.strip() for branch in row['rec_branch'].split(", ")]
        censuscode2011 = row['censuscode2011']
        for branch in branches:
            if branch in branch_villages:
                branch_villages[branch].add(censuscode2011)
            else:
                branch_villages[branch] = {censuscode2011}

# Convert sets to counts of unique villages
branch_village_counts = {branch: len(censuscode2011) for branch, censuscode2011 in branch_villages.items()}

# Convert the dictionary to a DataFrame
output_df = pd.DataFrame(list(branch_village_counts.items()), columns=['rec_branch', 'Unique Village Count'])

# Define a new file path to save the output
# new_file_path = r"C:\Users\Teja\Downloads\Vijval\Center_detail_latest5.xlsx"
new_file_path= f"{config.folder_path}\\Center_detail_latest5.xlsx"

# Save the DataFrame to a new Excel file
output_df.to_excel(new_file_path, sheet_name='Branch Village Counts', index=False)

# Provide the path to the updated file for download
new_file_path