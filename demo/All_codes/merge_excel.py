import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config
# The names of the files to merge
# file_names = [r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest1.xlsx",r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest2.xlsx", r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest3.xlsx", r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest7.xlsx"]
file_names = [f"{config.folder_path}\\Village_detail_latest1.xlsx",f"{config.folder_path}\\Village_detail_latest2.xlsx", f"{config.folder_path}\\Village_detail_latest3.xlsx", f"{config.folder_path}\\Village_detail_latest7.xlsx"]
# The name of the merged file
#merged_file_name = r"C:\Users\Vijval\Downloads\Village_detail_latest4.xlsx"
sheet_names = ['Village_names', 'Village_hits', 'Branch_village_count',"Village_censuscode"]
# The Excel file where the merged data will be saved
output_file = r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest4.xlsx"
# output_file = config.folder_path + "\\Village_detail_latest4.xlsx"

# Ensure the length of file_names and sheet_names match
assert len(file_names) == len(sheet_names), "Each file must have a corresponding sheet name."

# Initialize an Excel writer object
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for file_name, sheet_name in zip(file_names, sheet_names):
        # Read each Excel file
        df = pd.read_excel(file_name)

        # Write the data frame to a new sheet in the merged Excel file
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f'Merged Excel file saved as {output_file}')