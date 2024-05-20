# import pandas as pd
import sys
import os
sys.path.append('/path/to/directory')
import config
# # Replace 'file1.xlsx' and 'file2.xlsx' with the paths to your Excel files
# C:\Users\Teja\Desktop\karthik\demo\BR_APRIL1
# Get the parent directory of config.folder_path
parent_dir = os.path.dirname(config.folder_path)


names_br = ['Darbhanga','Sakri',
'Phulparas',
'Runnisaidpur',
'Benipur',
'Sahebganj',
'Rosera',
'Sheohar',
'Kanti',
'Sitamarhi',
'Samastipur']
names_ka = [
    'Kalaburgi',
'Basavakalyan',
'Yadgir',
'Bijapur',
'Kamalapur',
'Haveri',
'Belagavi',
'Chitguppa',
'Lokapur',
'Gokak',
'Shamanur',
'Hubbali',
'Shahpur',
'Ranebennur',
'Kittur'
]
names_up = [
    'Hathras',
'Jalesar',
'Shivpur',
'Gorakhpur',
'Chauri Chaura',
'Tundla',
'Aligarh',
'Ikauna',
'Khadda',
'Captainganj',
'Tarabganj',
'Mahoba',
'Nichlaul',
'Kiraoli'

]
import pandas as pd
for name in names_br:
    # Load DataFrames from Excel files
    # "C:\Users\Teja\Downloads\Vijval\centers"
    # file1_path = f'C:\\Users\\Teja\\Downloads\\Vijval\\centers\\{name}_Center_Map.xlsx'
    
    # file1_path = config.folder_path + "\\centers\\"+ f"{name}_Center_Map.xlsx"
    file1_path =f"{config.folder_path}\\centers\\{name}_Center_Map.xlsx"
    # file2_path = f'C:\\Users\\Teja\\Downloads\\Vijval\\villages\\{name}_Source_Map.xlsx'
    # file2_path = config.folder_path + "\\villages\\"+ f"{name}_Source_Map.xlsx"
    file2_path =f"{config.folder_path}\\villages\\{name}_Source_Map.xlsx"
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)
    # Remove duplicates from df1
    # df1 = df1.drop_duplicates(subset=['censuscode2011'])

    # Remove duplicates from df2
    # df2 = df2.drop_duplicates(subset=['censuscode2011'])
    # Convert 'lat_min_bound_centroid' and 'long_min_bound_centroid' to float64 in both DataFrames
    df1['lat_min_bound_centroid'] = pd.to_numeric(df1['lat_min_bound_centroid'], errors='coerce')
    df2['lat_min_bound_centroid'] = pd.to_numeric(df2['lat_min_bound_centroid'], errors='coerce')

    df1['long_min_bound_centroid'] = pd.to_numeric(df1['long_min_bound_centroid'], errors='coerce')
    df2['long_min_bound_centroid'] = pd.to_numeric(df2['long_min_bound_centroid'], errors='coerce')
    # Convert 'Pincode' column to object type in both dataframes
    df1['Pincode'] = df1['Pincode'].astype(str)
    df2['Pincode'] = df2['Pincode'].astype(str)

    # Now, you can try merging again
    result_df = pd.merge(df1, df2, on='Pincode', how='outer')

    # Now, perform the full outer join
    common_columns = df1.columns.intersection(df2.columns).tolist()
    result_df = pd.merge(df1, df2, on=common_columns, how='outer')
    

    # Remove duplicates based on specific columns
    # result_df = result_df.drop_duplicates(subset=['censuscode2011'])
    # Print 'Disbursed' column for specific census code
    # if (result_df['censuscode2011'] == '803207').all():
    #     print(result_df.loc[result_df['censuscode2011'] == '803207', 'Disbursed'])

    import pandas as pd
    import numpy as np

    # Assuming result_df is your DataFrame post-join
    # Fill NaN for specific columns
    result_df['center'] = result_df['center'].fillna('No_Center')
    result_df['Visited'] = result_df['Visited'].fillna('Yet-To-Visit')
    result_df = result_df.drop('state',axis=1)
    # Define a function to categorize Jun_23_Cat values
    def categorize_cat(value):
        if value in ['[nan]']:  # Correct way to check for NaN
            return "Unexplored"
        elif value in ['Categ-1', 'Categ-2', 'Categ-3', 'Categ-4', 'Categ-5']:
            return "Allowed"
        else:
            return "Not_Allowed"

    # Apply the categorization function to the Jun_23_Cat column
    result_df['Cat_Status'] = result_df['Jun_23_Cat'].apply(categorize_cat)

    # Create a new 'Key' column by concatenating 'Cat_Status', 'center', and 'Visited' with underscores
    result_df['Key'] = result_df['Cat_Status'] + '_' + result_df['center'] + '_' + result_df['Visited']

    # Optional: Convert entire DataFrame to strings if necessary and replace 'nan' with ''
    # This step might not be needed depending on your exact requirements
    result_df = result_df.replace(np.nan, '')  # Replace np.nan with empty strings globally if you prefer
    # "C:\Users\Teja\Downloads\Vijval\mixed"
    last_column_name = result_df.columns[-4]
    # print(last_column_name)
    # Drop the last column by its position
# This assumes the last column is the one to remove; adjust if the scenario changes
    result_df = result_df.drop(result_df.columns[-4], axis=1)
    # result_df.to_excel(f"{config.folder_path}\\mixedd\\{name}_Mixed_Map.xlsx", index=False)
    # Save the result to the parent directory in the 'mixedd' folder
    result_df.to_excel(os.path.join(parent_dir, "mixedd", f"{name}_Mixed_Map.xlsx"), index=False)
    # Save the result to a new Excel file
for name in names_ka:
    # Load DataFrames from Excel files
    # "C:\Users\Teja\Downloads\Vijval\centers"
    # file1_path = f'C:\\Users\\Teja\\Downloads\\Vijval\\centers\\{name}_Center_Map.xlsx'
    # file1_path = config.folder_path + "\\centers\\"+ f"{name}_Center_Map.xlsx"
    # file2_path = f'C:\\Users\\Teja\\Downloads\\Vijval\\villages\\{name}_Source_Map.xlsx'
    # file2_path = config.folder_path + "\\villages\\"+ f"{name}_Source_Map.xlsx"
    # file1_path = config.folder_path + "\\centers\\"+ f"{name}_Center_Map.xlsx"
    file1_path =f"{config.folder_path}\\centers\\{name}_Center_Map.xlsx"
    # file2_path = f'C:\\Users\\Teja\\Downloads\\Vijval\\villages\\{name}_Source_Map.xlsx'
    # file2_path = config.folder_path + "\\villages\\"+ f"{name}_Source_Map.xlsx"
    file2_path =f"{config.folder_path}\\villages\\{name}_Source_Map.xlsx"
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)
    # Remove duplicates from df1
    # df1 = df1.drop_duplicates(subset=['censuscode2011'])

    # Remove duplicates from df2
    # df2 = df2.drop_duplicates(subset=['censuscode2011'])
    # Convert 'lat_min_bound_centroid' and 'long_min_bound_centroid' to float64 in both DataFrames
    df1['lat_min_bound_centroid'] = pd.to_numeric(df1['lat_min_bound_centroid'], errors='coerce')
    df2['lat_min_bound_centroid'] = pd.to_numeric(df2['lat_min_bound_centroid'], errors='coerce')

    df1['long_min_bound_centroid'] = pd.to_numeric(df1['long_min_bound_centroid'], errors='coerce')
    df2['long_min_bound_centroid'] = pd.to_numeric(df2['long_min_bound_centroid'], errors='coerce')
    # Convert 'Pincode' column to object type in both dataframes
    df1['Pincode'] = df1['Pincode'].astype(str)
    df2['Pincode'] = df2['Pincode'].astype(str)

    # Now, you can try merging again
    result_df = pd.merge(df1, df2, on='Pincode', how='outer')

    # Now, perform the full outer join
    common_columns = df1.columns.intersection(df2.columns).tolist()
    result_df = pd.merge(df1, df2, on=common_columns, how='outer')
    

    # Remove duplicates based on specific columns
    # result_df = result_df.drop_duplicates(subset=['censuscode2011'])
    # Print 'Disbursed' column for specific census code
    # if (result_df['censuscode2011'] == '803207').all():
    #     print(result_df.loc[result_df['censuscode2011'] == '803207', 'Disbursed'])

    import pandas as pd
    import numpy as np

    # Assuming result_df is your DataFrame post-join
    # Fill NaN for specific columns
    result_df['center'] = result_df['center'].fillna('No_Center')
    result_df['Visited'] = result_df['Visited'].fillna('Yet-To-Visit')
    result_df = result_df.drop('state',axis=1)
    # Define a function to categorize Jun_23_Cat values
    def categorize_cat(value):
        if value in ['[nan]']:  # Correct way to check for NaN
            return "Unexplored"
        elif value in ['Categ-1', 'Categ-2', 'Categ-3', 'Categ-4', 'Categ-5']:
            return "Allowed"
        else:
            return "Not_Allowed"

    # Apply the categorization function to the Jun_23_Cat column
    result_df['Cat_Status'] = result_df['Jun_23_Cat'].apply(categorize_cat)

    # Create a new 'Key' column by concatenating 'Cat_Status', 'center', and 'Visited' with underscores
    result_df['Key'] = result_df['Cat_Status'] + '_' + result_df['center'] + '_' + result_df['Visited']

    # Optional: Convert entire DataFrame to strings if necessary and replace 'nan' with ''
    # This step might not be needed depending on your exact requirements
    result_df = result_df.replace(np.nan, '')  # Replace np.nan with empty strings globally if you prefer
    # "C:\Users\Teja\Downloads\Vijval\mixed"
    last_column_name = result_df.columns[-4]
    # Drop the last column by its position
# This assumes the last column is the one to remove; adjust if the scenario changes
    result_df = result_df.drop(result_df.columns[-4], axis=1)
    # print(last_column_name)
    # result_df.to_excel(f'C:\\Users\\Teja\\Desktop\\karthik\\demo\\mixedd\\{name}_Mixed_Map.xlsx', index=False)
    # result_df.to_excel(f"{config.folder_path}\\mixedd\\{name}_Mixed_Map.xlsx", index=False)
    # Save the result to the parent directory in the 'mixedd' folder
    result_df.to_excel(os.path.join(parent_dir, "mixedd", f"{name}_Mixed_Map.xlsx"), index=False)
    # Save the result to a new Excel file
for name in names_up:
    # Load DataFrames from Excel files
    # "C:\Users\Teja\Downloads\Vijval\centers"
    # file1_path = f'C:\\Users\\Teja\\Downloads\\Vijval\\centers\\{name}_Center_Map.xlsx'
    # file1_path = config.folder_path + "\\centers\\"+ f"{name}_Center_Map.xlsx"
    # file2_path = f'C:\\Users\\Teja\\Downloads\\Vijval\\villages\\{name}_Source_Map.xlsx'
    # file2_path = config.folder_path + "\\villages\\"+ f"{name}_Source_Map.xlsx"
    # file1_path = config.folder_path + "\\centers\\"+ f"{name}_Center_Map.xlsx"
    file1_path =f"{config.folder_path}\\centers\\{name}_Center_Map.xlsx"
    # file2_path = f'C:\\Users\\Teja\\Downloads\\Vijval\\villages\\{name}_Source_Map.xlsx'
    # file2_path = config.folder_path + "\\villages\\"+ f"{name}_Source_Map.xlsx"
    file2_path =f"{config.folder_path}\\villages\\{name}_Source_Map.xlsx"
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)
    # Remove duplicates from df1
    # df1 = df1.drop_duplicates(subset=['censuscode2011'])

    # Remove duplicates from df2
    # df2 = df2.drop_duplicates(subset=['censuscode2011'])
    # Convert 'lat_min_bound_centroid' and 'long_min_bound_centroid' to float64 in both DataFrames
    df1['lat_min_bound_centroid'] = pd.to_numeric(df1['lat_min_bound_centroid'], errors='coerce')
    df2['lat_min_bound_centroid'] = pd.to_numeric(df2['lat_min_bound_centroid'], errors='coerce')

    df1['long_min_bound_centroid'] = pd.to_numeric(df1['long_min_bound_centroid'], errors='coerce')
    df2['long_min_bound_centroid'] = pd.to_numeric(df2['long_min_bound_centroid'], errors='coerce')
    # Convert 'Pincode' column to object type in both dataframes
    df1['Pincode'] = df1['Pincode'].astype(str)
    df2['Pincode'] = df2['Pincode'].astype(str)

    # Now, you can try merging again
    result_df = pd.merge(df1, df2, on='Pincode', how='outer')

    # Now, perform the full outer join
    common_columns = df1.columns.intersection(df2.columns).tolist()
    result_df = pd.merge(df1, df2, on=common_columns, how='outer')
    

    # Remove duplicates based on specific columns
    # result_df = result_df.drop_duplicates(subset=['censuscode2011'])
    # Print 'Disbursed' column for specific census code
    # if (result_df['censuscode2011'] == '803207').all():
    #     print(result_df.loc[result_df['censuscode2011'] == '803207', 'Disbursed'])

    import pandas as pd
    import numpy as np

    # Assuming result_df is your DataFrame post-join
    # Fill NaN for specific columns
    result_df['center'] = result_df['center'].fillna('No_Center')
    result_df['Visited'] = result_df['Visited'].fillna('Yet-To-Visit')
    result_df = result_df.drop('state',axis=1)
    # Define a function to categorize Jun_23_Cat values
    def categorize_cat(value):
        if value in ['[nan]']:  # Correct way to check for NaN
            return "Unexplored"
        elif value in ['Categ-1', 'Categ-2', 'Categ-3', 'Categ-4', 'Categ-5']:
            return "Allowed"
        else:
            return "Not_Allowed"

    # Apply the categorization function to the Jun_23_Cat column
    result_df['Cat_Status'] = result_df['Jun_23_Cat'].apply(categorize_cat)

    # Create a new 'Key' column by concatenating 'Cat_Status', 'center', and 'Visited' with underscores
    result_df['Key'] = result_df['Cat_Status'] + '_' + result_df['center'] + '_' + result_df['Visited']

    # Optional: Convert entire DataFrame to strings if necessary and replace 'nan' with ''
    # This step might not be needed depending on your exact requirements
    result_df = result_df.replace(np.nan, '')  # Replace np.nan with empty strings globally if you prefer
    # "C:\Users\Teja\Downloads\Vijval\mixed"
    last_column_name = result_df.columns[-4]
    # print(last_column_name)
    # Drop the last column by its position
# This assumes the last column is the one to remove; adjust if the scenario changes
    result_df = result_df.drop(result_df.columns[-4], axis=1)
    # C:\Users\Teja\Desktop\karthik\demo\mixedd
    # result_df.to_excel(f'C:\\Users\\Teja\\Desktop\\karthik\\demo\\mixedd\\{name}_Mixed_Map.xlsx', index=False)
    # result_df.to_excel(f"{config.folder_path}\\mixedd\\{name}_Mixed_Map.xlsx", index=False)
    # Save the result to the parent directory in the 'mixedd' folder
    result_df.to_excel(os.path.join(parent_dir, "mixedd", f"{name}_Mixed_Map.xlsx"), index=False)
    # Save the result to a new Excel file
