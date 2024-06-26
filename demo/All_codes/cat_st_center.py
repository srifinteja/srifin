import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config
# Load the Excel files
# village_details_path = r"C:\Users\Teja\Downloads\Vijval\Center_detail_Latest1.xlsx"
village_details_path= f"{config.folder_path}\\Center_detail_Latest1.xlsx"
pincode_cats_path = "C:/Users/Teja/Downloads/Pincode Categories(Jun23-Feb24).xlsx"

village_details_df = pd.read_excel(village_details_path)
pincode_cats_df = pd.read_excel(pincode_cats_path)
last_column = pincode_cats_df.columns[-1]
# Merge to add 'Jun_23_Cat' as 'Cat' based on 'Pincode'
village_details_df = village_details_df.merge(pincode_cats_df[['Pincode', last_column]], on='Pincode', how='left')
village_details_df.rename(columns={last_column: 'Cat'}, inplace=True)

# Merge to add 'Jun_23_Cat' as 'Cat_tracked' based on 'Pincode_tracked'
village_details_df = village_details_df.merge(pincode_cats_df[['Pincode', last_column]], left_on='rec_pincode', right_on='Pincode', how='left')
village_details_df.rename(columns={last_column: 'Cat_tracked'}, inplace=True)

# Drop the extra 'Pincode' column added from the second merge
village_details_df.drop(columns=['Pincode_y'], inplace=True)
village_details_df.rename(columns={'Pincode_x': 'Pincode'}, inplace=True)

# Define the function for determining 'Status' and 'Status_Tracked'
def determine_status(category):
    allowed_categories = ['Categ-1', 'Categ-2', 'Categ-3', 'Categ-4','Categ-5']
    return 'Allowed' if category in allowed_categories else 'Not allowed'

# Create 'Status' and 'Status_Tracked' based on 'Cat' and 'Cat_tracked'
village_details_df['Status'] = village_details_df['Cat'].apply(determine_status)
village_details_df['Status_Tracked'] = village_details_df['Cat_tracked'].apply(determine_status)

# Save the updated DataFrame back to an Excel file
# output_path = r"C:\Users\Teja\Downloads\Vijval\Center_detail_Latest1.xlsx"
output_path= f"{config.folder_path}\\Center_detail_Latest1.xlsx"
village_details_df.to_excel(output_path, index=False)

print("Updated file saved to:", output_path)
