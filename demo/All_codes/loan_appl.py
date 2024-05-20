import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config
# Load the Excel files
# df1 = pd.read_excel(r"C:\Users\Teja\Downloads\Vijval\Center_detail_Latest3.xlsx")  # Adjust the path to your first Excel file
df1 = pd.read_excel(f"{config.folder_path}\\Center_detail_Latest3.xlsx")  # Adjust the path to your first Excel file
df2 = pd.read_csv(r"C:\Users\Teja\Downloads\25979d67-3481-4c53-94e8-96a92c6e6bd7.csv", low_memory=False)
  # Adjust the path to your second Excel file

# Clean or fill NaN values in 'center' and 'app_status' columns in df2
df2['center'] = df2['center'].fillna('')  # Replace NaN with empty strings or handle appropriately
df2['app_status'] = df2['app_status'].fillna('')  # Replace NaN with empty strings
# Convert the entire 'center_name' column to string
df2['center'] = df2['center'].astype(str)

# Remove '=' from the beginning of each string in 'center_name'
df2['center'] = df2['center'].apply(lambda x: x[1:] if x.startswith('=') else x)
# Split the entries in the 'All_centers' column and explode to normalize the data
all_centers_split = df1['All_centers'].str.split('; ').explode()

# Ensure each center from df1 is found at least once in df2's 'center' column to avoid KeyError
unique_centers = all_centers_split.unique()

# Initialize dictionary to hold the counts for each center
center_counts = {}

# List of specific statuses to track, now including CB_VERIFICATION_FAILED
statuses = ['CB_VERIFICATION_FAILED','CBC_DONE', 'CGT1', 'CGT2', 'GRT', 'DISBURSED']

# Initialize dictionaries to hold counts for each center and each status
status_counts = {status: {} for status in statuses}

for center in unique_centers:
    center_mask = df2['center'].str.contains(center, regex=False, na=False)
    center_counts[center] = center_mask.sum()
    
    # Loop through each status and update counts for the current center
    for status in statuses:
        # Count occurrences of each status for the current center
        status_counts[status][center] = df2.loc[center_mask, 'app_status'].eq(status).sum()

# Apply the total application counts back to df1
df1['Appl_count'] = df1['All_centers'].fillna('').apply(
    lambda centers: sum(center_counts.get(center, 0) for center in centers.split('; ') if center)
)

# Apply each status count to a new column in df1
for status in statuses:
    column_name = f"{status}_Count"
    df1[column_name] = df1['All_centers'].fillna('').apply(
        lambda centers: sum(status_counts[status].get(center, 0) for center in centers.split('; ') if center)
    )

# Optionally, save the modified DataFrame back to an Excel file
# df1.to_excel(r"C:\Users\Teja\Downloads\Vijval\Center_detail_Latest3.xlsx", index=False)
df1.to_excel(f"{config.folder_path}\\Center_detail_Latest3.xlsx", index=False)
