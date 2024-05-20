import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config
# Load the data
# df = pd.read_excel(r"C:\Users\Teja\Downloads\Vijval\Center_detail_Latest1.xlsx")
df = pd.read_excel(f"{config.folder_path}\\Center_detail_Latest1.xlsx")
print(df.shape)
df['rec_center_name'] = df['rec_center_name'].fillna('')
df['Population'] = df['Population'].fillna(0) 
df['House_hold'] = df['House_hold'].fillna(0) # For numerical columns, if 0 is an appropriate placeholder
df['Cat'] = df['Cat'].fillna('Unknown')
grouped = df.groupby(['censuscode2011', 'Village', 'Pincode', 'district', 'state', 'Population', 'House_hold', 'U/R', 'Cat','rec_branch'])

# Calculate the center_count for each group and reset index to turn the Series into a DataFrame
counts = grouped.size().reset_index(name='center_count')

# Initialize new columns for rec_center names based on status with empty strings
for col in ['Active_center', 'CGT1_center', 'CGT2_center', 'GRT_center', 'INITIATED_center']:
    counts[col] = ''

# Prepare a mapping from rec_center_status to the corresponding column name in the counts DataFrame
status_to_column = {
    'ACTIVE': 'Active_center',
    'CGT1': 'CGT1_center',
    'CGT2': 'CGT2_center',
    'GRT': 'GRT_center',
    'INITIATED': 'INITIATED_center'
}

# Iterate through original DataFrame to populate new columns based on rec_center_status
for _, row in df.iterrows():
    status = row['rec_center_status']
    rec_center_name = row['rec_center_name']
    key_columns = tuple(row[['censuscode2011', 'Village', 'Pincode', 'district', 'state', 'Population', 'House_hold', 'U/R', 'Cat','rec_branch']])
    
    # Find the index in counts DataFrame for the current group
    idx = counts[(counts[['censuscode2011', 'Village', 'Pincode', 'district', 'state', 'Population', 'House_hold', 'U/R', 'Cat', 'rec_branch']].apply(tuple, axis=1) == key_columns)].index
    
    if idx.empty:
        continue  # Skip if no matching group is found, though this should not happen

    idx = idx[0]  # Get the actual index value
    column_name = status_to_column.get(status)
    if column_name:
        # Append rec_center_name to the appropriate column, separated by semicolon if already populated
        if pd.notna(row['rec_center_name']):  # Check if rec_center_name is not NaN
            if counts.at[idx, column_name]:
                counts.at[idx, column_name] += '; ' + rec_center_name
            else:
                counts.at[idx, column_name] = rec_center_name

# Trim the last semicolon and space from the center names, if necessary
for col in ['Active_center', 'CGT1_center', 'CGT2_center', 'GRT_center', 'INITIATED_center']:
    counts[col] = counts[col].apply(lambda x: x.rstrip('; ') if isinstance(x, str) else x)

# Write the results to a new Excel file
# counts.to_excel("C:/Users/Teja/Downloads/Vijval/Center_detail_Latest3.xlsx", index=False)
counts.to_excel(f"{config.folder_path}\\Center_detail_Latest3.xlsx", index=False)
print('hello')
print(df.shape)