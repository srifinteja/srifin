import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config

##pincode without rec_ came from original village files
##pincode with rec_ came from geojson file
#now pincode is renamed to cat
#now rec_pincode is renamed to cat_tracked
#then cat1-5 are allowed else not allowed
# Load the Excel files
# C:\\Users\\Teja\\Desktop\\Karthik\\demo\\py_outputs\\
# village_details_path = r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest1.xlsx"
village_details_path= f"{config.folder_path}\\Village_detail_latest1.xlsx"
pincode_cats_path = r"C:/Users/Teja/Downloads/Pincode Categories(Jun23-Feb24).xlsx"

village_details_df = pd.read_excel(village_details_path)
print(village_details_df.columns)
pincode_cats_df = pd.read_excel(pincode_cats_path)
# Identify the last column in the pincode_cats_df DataFrame
last_column = pincode_cats_df.columns[-1]
# Merge to add 'Jun_23_Cat' as 'Cat' based on 'Pincode'
village_details_df = village_details_df.merge(pincode_cats_df[['Pincode', last_column]], on='Pincode', how='left')
print(village_details_df.columns)
village_details_df.rename(columns={last_column: 'Cat'}, inplace=True)
print(village_details_df.columns)
# Merge to add 'Jun_23_Cat' as 'Cat_tracked' based on 'Pincode_tracked'
village_details_df = village_details_df.merge(pincode_cats_df[['Pincode', last_column]], left_on='rec_Pincode', right_on='Pincode', how='left')
village_details_df.rename(columns={last_column: 'Cat_tracked'}, inplace=True)

# Drop the extra 'Pincode' column added from the second merge
village_details_df.drop(columns=['Pincode_y'], inplace=True)
village_details_df.rename(columns={'Pincode_x': 'Pincode'}, inplace=True)

# Define the function for determining 'Status' and 'Status_Tracked'
def determine_status(category):
    # Check if the input is not a scalar (for debugging purposes)
    # if isinstance(category, pd.Series):
    #     print("Error: determine_status received a Series instead of a scalar.")
    #     print(category)  # Print the Series to inspect it
    #     return 'Error'  # Return an error status or raise an exception

    allowed_categories = ['Categ-1', 'Categ-2', 'Categ-3', 'Categ-4', 'Categ-5']
    if str(category)=='nan':
        return 'NA'
    elif category in allowed_categories:
        return 'Allowed'
    else:
        return 'Not allowed'

# The part of your code where you apply determine_status
#village_details_df['Status'] = village_details_df['Cat'].apply(determine_status)

# Create 'Status' and 'Status_Tracked' based on 'Cat' and 'Cat_tracked'
village_details_df['Status'] = village_details_df['Cat'].apply(determine_status)
village_details_df['Status_Tracked'] = village_details_df['Cat_tracked'].apply(determine_status)

# Save the updated DataFrame back to an Excel file
# output_path = r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest1.xlsx"
output_path= f"{config.folder_path}\\Village_detail_latest1.xlsx"
village_details_df.to_excel(output_path, index=False)

print("Updated file saved to:", output_path)
