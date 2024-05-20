import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config

# Load the Excel file into a pandas DataFrame
# C:\Users\Teja\Desktop\Karthik\demo\py_outputs\
# df = pd.read_excel(r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest1.xlsx")
df = pd.read_excel(f"{config.folder_path}\\Village_detail_latest1.xlsx")
df['Population'] = df['Population'].fillna(0) 
df['House_hold'] = df['House_hold'].fillna(0) # For numerical columns, if 0 is an appropriate placeholder
df['Cat'] = df['Cat'].fillna('Unknown')

# Define the columns to check for repetition
columns_to_check = ['censuscode2011', 'Village', 'Pincode', 'district', 'state', 'Population', 'House_hold', 'U/R', 'Cat']
print(df.columns)
# Create a combined key for each row from the specified columns
df['Combined_Key'] = df[columns_to_check].astype(str).apply(lambda x: '-'.join(x), axis=1)

# Count the occurrences of each combined key
df['Hits'] = df.groupby('Combined_Key')['Combined_Key'].transform('size')
unique_df = df.drop_duplicates('Combined_Key')
branch_groups = df.groupby('Combined_Key')['rec_Branch'].unique().reset_index()
#print(branch_groups.loc[0:1])
#branch_groups['cnt'] = branch_groups.Branch.apply(lambda x: len(x))
#print(branch_groups[branch_groups['cnt']==branch_groups.cnt.max()])
#print(type(branch_groups.Branch))
final_df = pd.merge(unique_df, branch_groups, on='Combined_Key', how='left')
#print(final_df.loc[0:1])
final_columns = columns_to_check + ['Hits', 'rec_Branch_y']
final_df = final_df[final_columns]

# final_df.to_excel(r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest2.xlsx",index=False)
final_df.to_excel(f"{config.folder_path}\\Village_detail_latest2.xlsx",index=False)