import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config
# "C:\Users\Teja\Downloads\loan_app.csv"
# Load the Excel files
# file_path= config.folder_path + "\\Village_detail_latest2.xlsx"
# df1 = pd.read_excel(r"C:\Users\Teja\Downloads\Vijval\Center_detail_Latest3.xlsx")  # Adjust the path to your first Excel file
df1 = pd.read_excel(f"{config.folder_path}\\Center_detail_Latest3.xlsx")
# Load the first CSV file
df2_1 = pd.read_csv(r"C:\Users\Teja\Downloads\Axis_LA.csv")

# Load the second CSV file
df2_2 = pd.read_csv(r"C:\Users\Teja\Downloads\loan_app.csv")

# Combine the two dataframes
df2 = pd.concat([df2_1, df2_2], ignore_index=True)

# Assuming 'app_date', 'center', and 'app_status' are columns in the combined df2
# Convert 'app_date' to datetime format if not already done during loading
df2['app_date'] = pd.to_datetime(df2['app_date'], errors='coerce')

# Clean or fill NaN values in 'center' and 'app_status' columns in df2
df2['center'] = df2['center'].fillna('')  # Replace NaN with empty strings or handle appropriately
df2['app_status'] = df2['app_status'].fillna('')  # Replace NaN with empty strings
# df2['app_date'] = pd.to_datetime(df2['app_date'], errors='coerce')

# Split the entries in the 'All_centers' column and explode to normalize the data
all_centers_split = df1['All_centers'].str.split('; ').explode()

# Ensure each center from df1 is found at least once in df2's 'center' column to avoid KeyError
unique_centers = all_centers_split.unique()

# Initialize dictionary to hold the counts for each center
center_counts = {}

# List of specific statuses to track, now including CB_VERIFICATION_FAILED
statuses = ['CB_VERIFICATION_FAILED', 'CBC_DONE', 'CGT1', 'CGT2', 'GRT', 'DISBURSED']

# Initialize dictionaries to hold counts for each center and each status
status_counts = {status: {} for status in statuses}

for center in unique_centers:
    center_mask = df2['center'].str.contains(center, regex=False, na=False)
    center_counts[center] = center_mask.sum()
    
    # Loop through each status and update counts for the current center
    for status in statuses:
        # Count occurrences of each status for the current center
        status_counts[status][center] = df2.loc[center_mask, 'app_status'].eq(status).sum()

# Apply the total application counts back to df1
df1['Appl_count'] = df1['All_centers'].fillna('').apply(
    lambda centers: sum(center_counts.get(center, 0) for center in centers.split('; ') if center)
)

# Apply each status count to a new column in df1
for status in statuses:
    column_name = f"{status}_Count"
    df1[column_name] = df1['All_centers'].fillna('').apply(
        lambda centers: sum(status_counts[status].get(center, 0) for center in centers.split('; ') if center)
    )

# Get the latest application date for each center in df2
# latest_dates = df2.groupby('center')['app_date'].max()

# Get the latest application date for each center in df2
latest_dates = df2.groupby('center')['app_date'].max()

# Map the latest date back to each center in df1
df1['Latest_Appl_Date'] = df1['All_centers'].fillna('').apply(
    lambda centers: max(
        (latest_dates.get(center) for center in centers.split('; ') if center in latest_dates and pd.notna(latest_dates.get(center))),
        default=pd.NaT
    ).strftime('%m/%d/%Y') if any(
        center in latest_dates and pd.notna(latest_dates.get(center))
        for center in centers.split('; ')
    ) else None
)


# Optionally, save the modified DataFrame back to an Excel file
# df1.to_excel(r"C:\Users\Teja\Downloads\Vijval\Center_detail_Latest4.xlsx", index=False)
df1.to_excel(f"{config.folder_path}\\Center_detail_Latest4.xlsx", index=False)



# import pandas as pd
# import sys

# # Append the directory containing the config file to sys.path
# sys.path.append('/path/to/directory')
# import config

# # Error handling for file loading
# try:
#     df1 = pd.read_excel(config.folder_path + "\\Center_detail_Latest3.xlsx")
# except FileNotFoundError:
#     print("Failed to load Center_detail_Latest3.xlsx. Check if the file exists in the specified path.")
#     sys.exit(1)

# try:
#     df2_1 = pd.read_csv(r"C:\Users\Teja\Downloads\Axis_LA.csv")
#     df2_2 = pd.read_csv(r"C:\Users\Teja\Downloads\loan_app.csv")
# except FileNotFoundError as e:
#     print(f"Failed to load CSV files: {e}")
#     sys.exit(1)

# # Combine the two dataframes
# df2 = pd.concat([df2_1, df2_2], ignore_index=True)

# # Clean or fill NaN values in 'center' and 'app_status' columns in df2
# df2['center'] = df2['center'].fillna('')  # Replace NaN with empty strings
# df2['app_status'] = df2['app_status'].fillna('')  # Replace NaN with empty strings

# # Convert 'app_date' to datetime format if not already done during loading
# df2['app_date'] = pd.to_datetime(df2['app_date'], errors='coerce')

# # Split and normalize 'All_centers' entries
# df1['All_centers'] = df1['All_centers'].fillna('')
# all_centers_split = df1['All_centers'].str.split('; ').explode()

# # Avoid partial matches by using exact matches from the list of unique centers
# unique_centers = all_centers_split.unique()

# # Initialize dictionary for center counts
# center_counts = {center: 0 for center in unique_centers}

# # Initialize dictionaries to hold counts for each center and each status
# statuses = ['CB_VERIFICATION_FAILED', 'CBC_DONE', 'CGT1', 'CGT2', 'GRT', 'DISBURSED']
# status_counts = {status: {center: 0 for center in unique_centers} for status in statuses}

# # Populate counts for each center and status
# for center in unique_centers:
#     center_mask = df2['center'] == center  # Exact match
#     center_counts[center] = center_mask.sum()
    
#     for status in statuses:
#         status_counts[status][center] = df2.loc[center_mask, 'app_status'].eq(status).sum()

# # Apply the total application counts back to df1
# df1['Appl_count'] = df1['All_centers'].apply(
#     lambda centers: sum(center_counts.get(center, 0) for center in centers.split('; '))
# )

# # Apply each status count to a new column in df1
# for status in statuses:
#     column_name = f"{status}_Count"
#     df1[column_name] = df1['All_centers'].apply(
#         lambda centers: sum(status_counts[status].get(center, 0) for center in centers.split('; '))
#     )

# # Get the latest application date for each center in df2
# latest_dates = df2.groupby('center')['app_date'].max().dropna()

# # Map the latest date back to each center in df1
# df1['Latest_Appl_Date'] = df1['All_centers'].apply(
#     lambda centers: '; '.join(latest_dates.get(center).strftime('%m/%d/%Y') for center in centers.split('; ') if center in latest_dates)
#     if any(center in latest_dates for center in centers.split('; ')) else None
# )

# # Optionally, save the modified DataFrame back to an Excel file
# df1.to_excel(config.folder_path + "\\Center_detail_Latest4.xlsx", index=False)
