import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config
# Step 1: Read the Excel file
# df = pd.read_excel(r"C:\Users\Teja\Downloads\Vijval\Center_detail_Latest.xlsx")  # Replace 'path_to_your_excel_file.xlsx' with the actual path
df = pd.read_excel(f"{config.folder_path}\\Center_detail_Latest.xlsx")  # Replace 'path_to_your_excel_file.xlsx' with the actual path
# Step 2: Remove specified columns
columns_to_remove = [
    'zone', 'region', 'Village_left', 'Pincode_left', 'Remarks_left', 'district_left',
    'state_left', 'tot_p_2011_left', 'no_hh_2011_left', 'censuscode2011_left',
    'repayment_freq', 'meeting_place', 'partner_bank', 'address', 'close_data',
    'close_note', 'risk_rating', 'assigned_on', 'days_of_handling', 'ext_center_id',
    'collection_partner_id', 'createdAt', 'created_by', 'updatedAt', 'updated_by'
]
df.drop(columns=columns_to_remove, inplace=True, errors='ignore')  # errors='ignore' will ignore any columns not found

# Step 3: Rename columns by removing '_right'
columns_to_rename_right = {
    'Village_right': 'Village', 'Pincode_right': 'Pincode', 'Remarks_right': 'Remarks',
    'district_right': 'district', 'state_right': 'state', 'tot_p_2011_right': 'Population',
    'no_hh_2011_right': 'House_hold', 'censuscode2011_right': 'censuscode2011'
}
df.rename(columns=columns_to_rename_right, inplace=True)

# Step 4: Rename other specified columns by adding 'rec_'
columns_to_rename_rec = {
    'branch': 'rec_branch', 'id': 'rec_id', 'center_name': 'rec_center_name',
    'center_status': 'rec_center_status', 'center_day': 'rec_center_day',
    'center_time': 'rec_center_time','loan_officer': 'rec_loan_officer', 'Latitude': 'rec_Latitude', 'Longitude': 'rec_Longitude',
    'village_id': 'rec_village_id', 'pincode': 'rec_pincode', 'tru_2011': 'U/R'
}
df.rename(columns=columns_to_rename_rec, inplace=True)

# Save the modified DataFrame back to an Excel file, if needed

# df.to_excel(r"C:\Users\Teja\Downloads\Vijval\Center_detail_Latest1.xlsx", index=False)  # Replace 'modified_excel_file.xlsx' with your desired file name

df.to_excel(f"{config.folder_path}\\Center_detail_Latest1.xlsx", index=False)  # Replace 'modified_excel_file.xlsx' with your desired file name