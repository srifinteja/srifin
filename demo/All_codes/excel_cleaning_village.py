import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config
#removing additional columns and renaming columns

# Step 1: Read the Excel file
# C:\\Users\\Teja\\Desktop\\Karthik\\demo\\py_outputs\\
# df = pd.read_excel(r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest.xlsx")  # Replace 'path_to_your_excel_file.xlsx' with the actual path
df = pd.read_excel(f"{config.folder_path}\\Village_detail_latest.xlsx")  # Replace 'path_to_your_excel_file.xlsx' with the actual path

# Step 2: Remove specified columns
columns_to_remove = [
    'Village Status','Tehsil','Block','Mauja Name','Branch Distance(In Km)','Nearest Bank Distance(In Km)','Police Station Distance(In Km)','Road Type','Law and Order Status','Migration','Flood Affected Area','Total Population','No of Banks','No of Payment Banks','No of Small Finance Bank','No of MFI','Local Money Lenders','No of ATM','Local Language','Rural Flag','Remarks_left','Survey By','Survey On','Approved By','Approved On','Updated on','Updated By'
, 'Village_left', 'Pincode_left', 'Remarks_left', 'district_left',
    'state_left', 'tot_p_2011_left', 'no_hh_2011_left', 'censuscode2011_left','Remarks_right'
    
]
df.drop(columns=columns_to_remove, inplace=True, errors='ignore')  # errors='ignore' will ignore any columns not found

# Step 3: Rename columns by removing '_right'
columns_to_rename_right = {
    'Village_right': 'Village', 'Pincode_right': 'Pincode', 
    'district_right': 'district', 'state_right': 'state', 'tot_p_2011_right': 'Population',
    'no_hh_2011_right': 'House_hold', 'censuscode2011_right': 'censuscode2011', 'tru_2011':'U/R'
}
df.rename(columns=columns_to_rename_right, inplace=True)

# Step 4: Rename other specified columns by adding 'rec_'
#columns present in original villages files add recorded at the start.
columns_to_rename_rec = {
    'Branch': 'rec_Branch','Village ID': 'rec_VillageID','Village Name':'rec_VillageName','Pin code':'rec_Pincode','Latitude':'rec_Latitude','Longitude':'rec_Longitude','District':'rec_District','State':'rec_State'

}
df.rename(columns=columns_to_rename_rec, inplace=True)

# Save the modified DataFrame back to an Excel file, if needed
# df.to_excel(r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest1.xlsx", index=False)  # Replace 'modified_excel_file.xlsx' with your desired file name
df.to_excel(f"{config.folder_path}\\Village_detail_latest1.xlsx", index=False)  # Replace 'modified_excel_file.xlsx' with your desired file name