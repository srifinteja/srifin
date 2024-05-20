import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config
# Opt-in to the new behavior if you want to prepare for future versions
pd.set_option('future.no_silent_downcasting', True)
# Hathras
# Jalesar
# Shivpur
# Gorakhpur
# Chauri Chaura
# Tundla
# Aligarh
# Ikauna
# Khadda
# Captainganj
# Tarabganj
# Mahoba
# Nichlaul
# Kiraoli
# Fatehabad

# Kalaburgi
# Basavakalyan
# Yadgir
# Bijapur
# Kamalapur
# Haveri
# Belagavi
# Chitguppa
# Lokapur
# Gokak
# Shamanur
# Hubbali
# Shahpur
# Ranebennur
# Kittur




villages_up = ['Aligarh', 'Ayodhya', 'Shikarpur','Hathras','Jalesar','Shivpur','Gorakhpur','Chauri Chaura','Tundla','Ikauna','Khadda','Captainganj','Tarabganj','Mahoba','Nichlaul','Kiraoli','Fatehabad']
villages_ka = ['Kalaburgi', 'Basavakalyan', 'Yadgir', 'Bijapur', 'Kamalapur', 'Haveri', 
            'Belagavi', 'Chitguppa', 'Lokapur', 'Gokak', 'Shamanur', 'Hubbali', 
            'Shahpur', 'Ranebennur', 'Kittur']
villages_br = [ 'Darbhanga', 'Sakri', 'Phulparas', 
            'Runnisaidpur', 'Benipur', 'Sahebganj', 'Rosera', 'Sheohar', 'Kanti', 
            'Sitamarhi', 'Samastipur']
villag = villages_br+villages_ka+villages_up
# print(villag)
states=['UP','BR','KA']
# villages = [villages_up,villages_ka,villages_br]
# Load the second Excel file
file2_path = r"C:\Users\Teja\Downloads\Vijval\Final_Output_Axis_26th.xlsx"
# file2_path =config.folder_path + "\\Final_Output_Axis_26th.xlsx"
df2 = pd.read_excel(file2_path, sheet_name='Center_censuscode')

# Specify columns to merge and select from the second file
merge_columns = ['censuscode2011']
selected_columns = ['center_count', 'Active_center', 'CGT1_center', 'CGT2_center',
                    'GRT_center', 'INITIATED_center', 'All_centers', 'bcode',
                    'Appl_count', 'CB_VERIFICATION_FAILED_Count', 'CBC_DONE_Count', 
                    'CGT1_Count', 'CGT2_Count', 'GRT_Count', 'DISBURSED_Count']

# List of columns to fill with 0
columns_to_fill = ['Center_count', 'INITIATED_Cen', 'CGT1_Cen', 'CGT2_Cen','GRT_Cen','Active_Cen','Loan_apps','CB_fail','CB_done','CGT1','CGT2','GRT','Disbursed','Population','HouseHolds']  
# Loop through each state and its corresponding villages
for village in villages_up:
    # Load the first Excel file
    # file1_path = rf"C:\Users\Teja\Downloads\30km_Branches_Surroundings\UP_30km\{village}_30_km.xlsx"
    file1_path = rf"C:\Users\Teja\Downloads\30km_Branches_Surroundings\UP_30km\{village}_30_km.xlsx"
    df1 = pd.read_excel(file1_path)

    # Merge dataframes based on censuscode2011 column
    merged_df = pd.merge(df1, df2[merge_columns + selected_columns],
                        on='censuscode2011', how='left')

    # Add Centre_status column based on match
    merged_df['Centre_status'] = merged_df.apply(lambda row: 'Center_Exists'
                                                if pd.notna(row['center_count'])
                                                else 'No_Center', axis=1)

    # Define the columns to remove
    columns_to_remove = ['All_centers', 'bcode', 'alpha_70_stat', 'poly_valid']

    # Remove the specified columns from merged_df
    merged_df = merged_df.drop(columns=columns_to_remove)

    # Rename columns
    merged_df = merged_df.rename(columns={
        'tot_p_2011': 'Population',
        'no_hh_2011': 'HouseHolds',
        'center_count': 'Center_count',
        'Active_center': 'Active_Cen',
        'CGT1_center': 'CGT1_Cen',
        'CGT1_Count': 'CGT1',
        'CGT2_Count': 'CGT2',
        'GRT_Count': 'GRT',
        'DISBURSED_Count': 'Disbursed',
        'CBC_DONE_Count': 'CB_done',
        'CGT2_center': 'CGT2_Cen',
        'GRT_center': 'GRT_Cen',
        'Appl_count': 'Loan_apps',
        'tru_2011': 'U/R',
        'district': 'District',
        'Final_Cat': 'Jun_23_Cat',
        'INITIATED_center': 'INITIATED_Cen',
        'Centre_status': 'center',
        'CB_VERIFICATION_FAILED_Count': 'CB_fail'
    })

    # Reorder columns
    new_order = ['censuscode2011', 'Village', 'Pincode', 'District', 'state', 'Population',
                'HouseHolds', 'U/R', 'lat_min_bound_centroid', 'long_min_bound_centroid',
                'Jun_23_Cat', 'Center_count', 'INITIATED_Cen', 'CGT1_Cen',
                'CGT2_Cen', 'GRT_Cen', 'Active_Cen', 'Loan_apps', 'CB_fail', 'CB_done',
                'CGT1', 'CGT2', 'GRT', 'Disbursed', 'center']

    # Select columns in the new order
    merged_df = merged_df[new_order]

    # Fill blank cells in multiple columns with 0
    for column in columns_to_fill:
        merged_df[column] = merged_df[column].fillna(0)

    # Save the modified dataframe back to Excel or use it as needed
    # merged_df.to_excel(rf'C:\Users\Teja\Downloads\Vijval\centers\{village}_Center_Map.xlsx', index=False)
    # merged_df.to_excel(config.folder_path +"\\centers" +"\\{village}_Center_Map.xlsx", index=False)
    output_path = f"{config.folder_path}\\centers\\{village}_Center_Map.xlsx"
    merged_df.to_excel(output_path, index=False)
    
for village in villages_ka:
    # Load the first Excel file
    file1_path = rf"C:\Users\Teja\Downloads\30km_Branches_Surroundings\KA_30km\{village}_30_km.xlsx"
    df1 = pd.read_excel(file1_path)

    # Merge dataframes based on censuscode2011 column
    merged_df = pd.merge(df1, df2[merge_columns + selected_columns],
                        on='censuscode2011', how='left')

    # Add Centre_status column based on match
    merged_df['Centre_status'] = merged_df.apply(lambda row: 'Center_Exists'
                                                if pd.notna(row['center_count'])
                                                else 'No_Center', axis=1)

    # Define the columns to remove
    columns_to_remove = ['All_centers', 'bcode', 'alpha_70_stat', 'poly_valid']

    # Remove the specified columns from merged_df
    merged_df = merged_df.drop(columns=columns_to_remove)

    # Rename columns
    merged_df = merged_df.rename(columns={
        'tot_p_2011': 'Population',
        'no_hh_2011': 'HouseHolds',
        'center_count': 'Center_count',
        'Active_center': 'Active_Cen',
        'CGT1_center': 'CGT1_Cen',
        'CGT1_Count': 'CGT1',
        'CGT2_Count': 'CGT2',
        'GRT_Count': 'GRT',
        'DISBURSED_Count': 'Disbursed',
        'CBC_DONE_Count': 'CB_done',
        'CGT2_center': 'CGT2_Cen',
        'GRT_center': 'GRT_Cen',
        'Appl_count': 'Loan_apps',
        'tru_2011': 'U/R',
        'district': 'District',
        'Final_Cat': 'Jun_23_Cat',
        'INITIATED_center': 'INITIATED_Cen',
        'Centre_status': 'center',
        'CB_VERIFICATION_FAILED_Count': 'CB_fail'
    })

    # Reorder columns
    new_order = ['censuscode2011', 'Village', 'Pincode', 'District', 'state', 'Population',
                'HouseHolds', 'U/R', 'lat_min_bound_centroid', 'long_min_bound_centroid',
                'Jun_23_Cat', 'Center_count', 'INITIATED_Cen', 'CGT1_Cen',
                'CGT2_Cen', 'GRT_Cen', 'Active_Cen', 'Loan_apps', 'CB_fail', 'CB_done',
                'CGT1', 'CGT2', 'GRT', 'Disbursed', 'center']

    # Select columns in the new order
    merged_df = merged_df[new_order]

    # Fill blank cells in multiple columns with 0
    for column in columns_to_fill:
        merged_df[column] = merged_df[column].fillna(0)

    # Save the modified dataframe back to Excel or use it as needed
    # merged_df.to_excel(rf'C:\Users\Teja\Downloads\Vijval\centers\{village}_Center_Map.xlsx', index=False)
    # merged_df.to_excel(config.folder_path +"\\centers" +"\\{village}_Center_Map.xlsx", index=False)
    output_path = f"{config.folder_path}\\centers\\{village}_Center_Map.xlsx"
    merged_df.to_excel(output_path, index=False)
for village in villages_br:
    # Load the first Excel file
    file1_path = rf"C:\Users\Teja\Downloads\30km_Branches_Surroundings\BR_30km\{village}_30_km.xlsx"
    df1 = pd.read_excel(file1_path)

    # Merge dataframes based on censuscode2011 column
    merged_df = pd.merge(df1, df2[merge_columns + selected_columns],
                        on='censuscode2011', how='left')

    # Add Centre_status column based on match
    merged_df['Centre_status'] = merged_df.apply(lambda row: 'Center_Exists'
                                                if pd.notna(row['center_count'])
                                                else 'No_Center', axis=1)

    # Define the columns to remove
    columns_to_remove = ['All_centers', 'bcode', 'alpha_70_stat', 'poly_valid']

    # Remove the specified columns from merged_df
    merged_df = merged_df.drop(columns=columns_to_remove)

    # Rename columns
    merged_df = merged_df.rename(columns={
        'tot_p_2011': 'Population',
        'no_hh_2011': 'HouseHolds',
        'center_count': 'Center_count',
        'Active_center': 'Active_Cen',
        'CGT1_center': 'CGT1_Cen',
        'CGT1_Count': 'CGT1',
        'CGT2_Count': 'CGT2',
        'GRT_Count': 'GRT',
        'DISBURSED_Count': 'Disbursed',
        'CBC_DONE_Count': 'CB_done',
        'CGT2_center': 'CGT2_Cen',
        'GRT_center': 'GRT_Cen',
        'Appl_count': 'Loan_apps',
        'tru_2011': 'U/R',
        'district': 'District',
        'Final_Cat': 'Jun_23_Cat',
        'INITIATED_center': 'INITIATED_Cen',
        'Centre_status': 'center',
        'CB_VERIFICATION_FAILED_Count': 'CB_fail'
    })

    # Reorder columns
    new_order = ['censuscode2011', 'Village', 'Pincode', 'District', 'state', 'Population',
                'HouseHolds', 'U/R', 'lat_min_bound_centroid', 'long_min_bound_centroid',
                'Jun_23_Cat', 'Center_count', 'INITIATED_Cen', 'CGT1_Cen',
                'CGT2_Cen', 'GRT_Cen', 'Active_Cen', 'Loan_apps', 'CB_fail', 'CB_done',
                'CGT1', 'CGT2', 'GRT', 'Disbursed', 'center']

    # Select columns in the new order
    merged_df = merged_df[new_order]

    # Fill blank cells in multiple columns with 0
    for column in columns_to_fill:
        merged_df[column] = merged_df[column].fillna(0)

    # Save the modified dataframe back to Excel or use it as needed
    # merged_df.to_excel(rf'C:\Users\Teja\Downloads\Vijval\centers\{village}_Center_Map.xlsx', index=False)
    output_path = f"{config.folder_path}\\centers\\{village}_Center_Map.xlsx"
    merged_df.to_excel(output_path, index=False)
    # merged_df.to_excel(config.folder_path + "\\centers"+"\\{village}_Center_Map.xlsx", index=False)
