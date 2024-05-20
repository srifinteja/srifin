import pandas as pd
import ast
import sys
sys.path.append('/path/to/directory')
import config
# Load the Excel files into pandas DataFrames
# Desktop\Karthik\demo\py_outputs\
# df_by = pd.read_excel(r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest2.xlsx", sheet_name='Sheet1')
df_by= pd.read_excel(f"{config.folder_path}\\Village_detail_latest2.xlsx",sheet_name='Sheet1')
df_bcode = pd.read_excel(r"C:\Users\Teja\Downloads\Existing_Branches (2).xlsx", sheet_name='B_Codes')

df_by['rec_Branch_y'] = df_by['rec_Branch_y'].str.replace(' ', ', ', regex=False)
df_by['rec_Branch_y'] = df_by['rec_Branch_y'].apply(ast.literal_eval)

df_by_exploded = df_by.explode('rec_Branch_y')

df_merged = df_by_exploded.merge(df_bcode, left_on='rec_Branch_y', right_on='bcode', how='left')

df_by['Branch Names'] = df_merged.groupby(df_by_exploded.index)['Branch Name'].agg(lambda x: ', '.join(x.dropna()))



# Write the updated df_by to a new Excel file
# output_file_path = r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest2.xlsx"  # Replace with the desired path for the updated file
output_file_path= f"{config.folder_path}\\Village_detail_latest2.xlsx"
df_by.to_excel(output_file_path, index=False)
print("hi")
