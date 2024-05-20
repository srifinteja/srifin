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

