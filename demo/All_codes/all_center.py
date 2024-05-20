import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config
# Step 1: Load the Excel file
# file_path = r'C:\Users\Teja\Downloads\Vijval\Center_detail_Latest3.xlsx'  # Update this to your Excel file path
file_path = config.folder_path + "\\Center_detail_Latest3.xlsx"
df = pd.read_excel(file_path)

# Step 2: Combine the specified columns into one string for each row
# Adjust the lambda function to filter out empty strings before joining
df['All_centers'] = df[['Active_center', 'CGT1_center', 'CGT2_center', 'GRT_center', 'INITIATED_center']].apply(
    lambda x: '; '.join([i for i in x.dropna().astype(str) if i.strip()]), axis=1)
# Step 3: Save the modified DataFrame back to an Excel file
# You might want to specify a different file name to save the updated data as a new file
# output_file_path = r"C:\Users\Teja\Downloads\Vijval\Center_detail_Latest3.xlsx" # Update this to your desired output file path
output_file_path = config.folder_path + "\\Center_detail_Latest3.xlsx"
df.to_excel(output_file_path, index=False)
print("hi")
