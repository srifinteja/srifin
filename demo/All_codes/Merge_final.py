import pandas as pd
import xlsxwriter
import sys
sys.path.append('/path/to/directory')
import config

# Paths to your Excel files
# excel_path1 = r"C:\Users\Teja\Downloads\Vijval\Village_detail_latest4.xlsx"
# excel_path2 = r"C:\Users\Teja\Downloads\Vijval\Center_detail_latest6.xlsx"
excel_path1 = f"{config.folder_path}\\Village_detail_latest4.xlsx"
excel_path2 = f"{config.folder_path}\\Center_detail_latest6.xlsx"
# Load all sheets from both Excel files
xls1 = pd.ExcelFile(excel_path1)
xls2 = pd.ExcelFile(excel_path2)

# Get sheet names for both Excel files
sheets1 = xls1.sheet_names
sheets2 = xls2.sheet_names

# Create a new Excel writer object
# output_excel_path = r"C:\Users\Teja\Downloads\Vijval\Final_Output_Axis_26th.xlsx"
output_excel_path =f"{config.folder_path}\\Final_Output_Axis_26th.xlsx"
with pd.ExcelWriter(output_excel_path, engine='xlsxwriter') as writer:

    # Iterate over sheets in the first Excel file
    for sheet_name in sheets1:
        # Read the current sheet from the first Excel file
        df1 = pd.read_excel(xls1, sheet_name)
        
        # Check if the current sheet name exists in the second Excel file and merge
        if sheet_name in sheets2:
            df2 = pd.read_excel(xls2, sheet_name)
            # Assuming you want to concatenate the sheets vertically
            merged_df = pd.concat([df1, df2], ignore_index=True)
        else:
            merged_df = df1
        
        # Write the merged DataFrame to a sheet in the new Excel file
        merged_df.to_excel(writer, sheet_name=sheet_name, index=False)

    # Check for sheets in the second Excel file that weren't in the first and add them
    for sheet_name in sheets2:
        if sheet_name not in sheets1:
            df = pd.read_excel(xls2, sheet_name)
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    # Save the new Excel file
    # writer.close()


    print(f"Merged Excel file has been saved to: {output_excel_path}")
    print("done")
