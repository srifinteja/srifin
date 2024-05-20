import os
import shutil
import subprocess
import sys
sys.path.append('/path/to/directory')
import config
# Specify the directory from which to delete all files
# folder = 'C:\\Users\\Teja\\Downloads\\Vijval'
folder =config.folder_path 

# Define the names of the folders to create
folders_to_create = ['centers', 'villages']

# Create the folders if they do not exist
for folder_name in folders_to_create:
    folder_path = os.path.join(folder, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")
# Iterate over each item in the directory
for item in os.listdir(folder):
    item_path = os.path.join(folder, item)  # Get the full path to the item
    try:
        if os.path.isfile(item_path):  # Check if it's a file
            os.unlink(item_path)  # Remove the file
        # Directories are not deleted, only files are
    except Exception as e:
        print(f'Failed to delete {item_path}. Reason: {e}')


# Base directory where all scripts are stored
base_path = r'C:\Users\Teja\Desktop\karthik\demo\All_codes'
# List of Python scripts to run in order
scripts = [
    
    'Village_detail_2.py',
    'add_Tru.py',
    'excel_cleaning_village.py',
    'Cat_Status.py',
    'test.py',
    'branch_name_from_bcode.py',
    'village_state-hits.py',
    'Branch_village_count.py',
    'censuscode_merge_village.py',
    'merge_excel.py',
    'Center_details_2.py',
    'add_Tru_center.py',
    'excel_cleaning.py',
    'cat_st_center.py',
    'CENTERCOUNT.py',
    'all_center.py',
    'Bcode_from_BName.py',
    'loan_appl.py',
    'Center_last.py',
    
    'censuscode_merge_center.py',
    'center_village_count.py',
    'Center_state_hits.py',
    'merge_center.py',
    'Merge_final.py',
    'final_mix.py',
    'centermix.py',
    'xx.py'
    # 'Center_state_hits.py',
    # 'village_state-hits.py',
    # 'state_hit_final.py'
    


    # Add more script file names as needed
]
for script in scripts:
    # Construct the full path for each script
    script_path = os.path.join(base_path, script)
    print(f"Running {script_path}")
    # Execute the Python script
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    
    # Print output and handle potential errors
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(f"Error in {script}: {result.stderr}")

print("All scripts executed!!!!!!!!!!!!!!!!!!!")