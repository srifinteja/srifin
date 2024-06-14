# import pandas as pd
# import sys
# sys.path.append('/path/to/directory')
# import config
# # Load the first Excel file
# # file1 = r"C:\Users\Teja\Downloads\Vijval\Center_detail_Latest3.xlsx"
# file1= f"{config.folder_path}\\Center_detail_Latest3.xlsx"
# df1 = pd.read_excel(file1)

# # Load the second Excel file
# file2 = r"C:\Users\Teja\Downloads\Existing_Branches (2).xlsx"
# df2 = pd.read_excel(file2,sheet_name='B_Codes')

# # Merge the DataFrames based on the matching branch names
# # Assuming 'rec_branch' is in df1 and 'Branch Name' and 'Bcode' are in df2
# merged_df = pd.merge(df1, df2, left_on='rec_branch', right_on='Branch Name',how="left")
# # merged_df.drop(columns=['bcode_y'],inplace=True)
# # merged_df.rename(columns={'bcode_x':'bcode'},inplace=True)
# print(merged_df.columns)
# # Now you can select the columns you want to keep in the new sheet
# # For example, keeping all columns from df1 and the 'Bcode' from df2
# final_df = merged_df[df1.columns.tolist() + ['bcode']]

# # Write the result to a new sheet in the first Excel file
# # Note: This creates a new file. If you want to append it to the existing file, you'll need to use ExcelWriter with mode='a'
# # output_file = r"C:\Users\Teja\Downloads\Vijval\Center_detail_Latest3.xlsx"
# output_file = f"{config.folder_path}\\Center_detail_Latest3.xlsx"
# with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
#     final_df.to_excel(writer, sheet_name='NewSheet', index=False)

# print("Task completed. The data has been written to the new sheet in the first Excel file.")
import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config

file1 = f"{config.folder_path}\\Center_detail_Latest3.xlsx"
file2 = r"C:\Users\Teja\Downloads\Existing_Branches (2).xlsx"

# Load the first Excel file
try:
    df1 = pd.read_excel(file1)
    print("First Excel file loaded successfully.")
except Exception as e:
    print(f"Error loading first Excel file: {e}")

# Load the second Excel file
try:
    df2 = pd.read_excel(file2, sheet_name='B_Codes')
    print("Second Excel file loaded successfully.")
except Exception as e:
    print(f"Error loading second Excel file: {e}")

# Merge the DataFrames based on the matching branch names
try:
    merged_df = pd.merge(df1, df2, left_on='rec_branch', right_on='Branch Name', how="left")
    print("DataFrames merged successfully.")
    print(merged_df.columns)

    # Rename the 'bcode_x' or 'bcode_y' column to 'bcode' if it exists
    if 'bcode_x' in merged_df.columns:
        merged_df.rename(columns={'bcode_x': 'bcode'}, inplace=True)
    elif 'bcode_y' in merged_df.columns:
        merged_df.rename(columns={'bcode_y': 'bcode'}, inplace=True)

    # Check the columns again after renaming
    print("Columns after renaming:")
    print(merged_df.columns)

    # Now you can select the columns you want to keep in the new sheet
    final_df = merged_df[df1.columns.tolist() + ['bcode']]

    # Write the result to a new sheet in the first Excel file
    output_file = f"{config.folder_path}\\Center_detail_Latest3.xlsx"
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        final_df.to_excel(writer, sheet_name='NewSheet', index=False)

    print("Task completed. The data has been written to the new sheet in the first Excel file.")
except Exception as e:
    print(f"Error during processing: {e}")
