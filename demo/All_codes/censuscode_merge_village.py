import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config
# Replace 'your_excel_file.xlsx' with the actual path to your Excel file
# file_path = r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest2.xlsx"
file_path= f"{config.folder_path}\\Village_detail_latest2.xlsx"
# output_file_path = r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest7.xlsx"
output_file_path= f"{config.folder_path}\\Village_detail_latest7.xlsx"
# Load the data from the Excel file
df = pd.read_excel(file_path)
df['censuscode2011'] = df['censuscode2011'].fillna(0)
# Assuming that by 'merge the remaining column', you mean concatenate the unique values
# This function will concatenate unique non-null values from a Series into a string
def merge_unique(series):
    return '; '.join(series.dropna().astype(str).unique())

# Group by 'censuscode2011' and aggregate the data
grouped_df = df.groupby('censuscode2011', as_index=False).agg({
    'Village': merge_unique,  # Assuming the Village name does not change within the same censuscode2011
    'Pincode': merge_unique,  # Assuming the Pincode does not change within the same censuscode2011
    'district': merge_unique,  # Assuming the district does not change within the same censuscode2011
    'state': merge_unique,  # Assuming the state does not change within the same censuscode2011
    'Population': merge_unique,  # Summing up the Population for the same censuscode2011
    'House_hold': merge_unique,  # Summing up the House_hold for the same censuscode2011
    'U/R': merge_unique,  # Assuming U/R does not change within the same censuscode2011
    'Cat': merge_unique,  # Assuming Cat does not change within the same censuscode2011
    'Branch Names': merge_unique,  # Merging unique Branch Names for the same censuscode2011
})

# Write the resulting DataFrame to a new Excel file
grouped_df.to_excel(output_file_path, index=False)
