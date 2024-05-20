import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config
# Read the original Excel file
#df = pd.read_excel(r"C:\Users\Vijval\Downloads\Village_detail_latest2.xlsx")

# Function to filter and save relevant rows based on state and category
# Load the main data Excel file
# main_df = pd.read_excel(r"C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Village_detail_latest2.xlsx")
main_df = pd.read_excel(f"{config.folder_path}\\Village_detail_latest2.xlsx")

# Adjust 'Branch Names' to consider only the first element (assuming comma-separated)
main_df['FirstBranchName'] = main_df['Branch Names'].apply(lambda x: x.split(',')[0].strip() if pd.notnull(x) else '')

# Define a function to filter by state and category, then save
def filter_by_state_and_category(state_name, categories, output_filename):
    filtered_df = main_df[(main_df['state'] == state_name) & (main_df['Cat'].isin(categories))]
    filtered_df.to_excel(output_filename, index=False)

# Define a function to handle Uttar Pradesh specific logic
def handle_uttar_pradesh():
    # Categories of interest
    categories = ['Categ-6', 'Categ-7', 'Unknown']
    
    # Load the Existing Branches Excel file, "UP" sheet
    branches_df = pd.read_excel(r"C:\Users\Teja\Downloads\Existing_Branches (2).xlsx", sheet_name='UP')
    
    # Merge with the branches information based on 'FirstBranchName'
    merged_df = pd.merge(main_df[main_df['state'] == 'Uttar Pradesh'], branches_df, left_on='FirstBranchName', right_on='Branch', how='inner')
    
    # Filter for the specified categories
    merged_df = merged_df[merged_df['Cat'].isin(categories)]
    
    # Split based on 'Half' and save
    east_df = merged_df[merged_df['Half'] == 'East']
    west_df = merged_df[merged_df['Half'] == 'West']
    
    east_df.to_excel(f"{config.folder_path}\\Village_UP_East.xlsx", index=False)
    west_df.to_excel(f"{config.folder_path}\\Village_UP_West.xlsx", index=False)

# Categories of interest
categories_of_interest = ['Categ-6', 'Categ-7', 'Unknown']

# Filter and save for Bihar and Karnataka
filter_by_state_and_category('Bihar', categories_of_interest, 'C:\\Users\\Teja\\Desktop\\Karthik\\demo\\py_outputs\\Village_Bihar_hits.xlsx')
filter_by_state_and_category('Karnataka', categories_of_interest, 'C:\\Users\\Teja\\Desktop\\Karthik\\demo\\py_outputs\\Village_Karnataka_hits.xlsx')

# Handle Uttar Pradesh specific filtering and saving
handle_uttar_pradesh()

