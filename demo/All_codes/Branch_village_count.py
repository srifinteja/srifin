import pandas as pd
from openpyxl import load_workbook
import sys
sys.path.append('/path/to/directory')
import config

#how many villages a branch cover
#for each branch how many villages
# Load the Excel file
# C:\Users\Teja\Desktop\Karthik\demo\py_outputs\
# file_path = r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest2.xlsx"
file_path= f"{config.folder_path}\\Village_detail_latest2.xlsx"
df = pd.read_excel(file_path)

branch_villages = {}

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    if pd.notna(row['Branch Names']):
        branches = [branch.strip() for branch in row['Branch Names'].split(", ")]
        village = row['Village']
        for branch in branches:
            if branch in branch_villages:
                branch_villages[branch].add(village)
            else:
                branch_villages[branch] = {village}

# Convert sets to counts of unique villages
branch_village_counts = {branch: len(villages) for branch, villages in branch_villages.items()}

# Convert the dictionary to a DataFrame
output_df = pd.DataFrame(list(branch_village_counts.items()), columns=['Branch Name', 'Unique Village Count'])

# Define a new file path to save the output
# new_file_path = r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest3.xlsx"
new_file_path= f"{config.folder_path}\\Village_detail_latest3.xlsx"
# Save the DataFrame to a new Excel file
output_df.to_excel(new_file_path, sheet_name='Branch Village Counts', index=False)

# Provide the path to the updated file for download
new_file_path