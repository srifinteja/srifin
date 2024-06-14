import pandas as pd
import sys
sys.path.append('/path/to/directory')
import config
villages_up = ['Aligarh','Shahjahanpur', 'Banda','Jhansi','Lalitpur','Hamirpur','Mathura','Baraut','Meerganj','Ayodhya','Mawana','Siyana','Nanpara','Gopiganj','Bahraich','Balrampur','Uruwa Bazar','Tetari Bazar', 'Madhuban','Shikarpur','Hathras','Jalesar','Shivpur','Gorakhpur','Chauri Chaura','Tundla','Ikauna','Khadda','Captainganj','Tarabganj','Mahoba','Nichlaul','Kiraoli','Fatehabad']
villages_ka = ['Kalaburgi', 'Basavakalyan', 'Yadgir', 'Bijapur', 'Kamalapur', 'Haveri', 
            'Belagavi', 'Chitguppa', 'Lokapur', 'Gokak', 'Shamanur', 'Hubbali', 
            'Shahpur', 'Ranebennur', 'Kittur']
villages_br = [ 'Darbhanga', 'Sakri', 'Phulparas', 
            'Runnisaidpur', 'Benipur', 'Sahebganj', 'Rosera', 'Sheohar', 'Kanti', 
            'Sitamarhi', 'Samastipur']
villag = villages_br+villages_ka+villages_up

columns_to_fill = ['Population','Households']  
# print(villag)s
states=['UP','BR','KA']
for village in villages_up:
    # Load the first Excel file (as per your description df1 should be the second file and df2 the first file)
    df2 = pd.read_excel(rf'C:\Users\Teja\Downloads\30km_Branches_Surroundings\UP_30km\{village}_30_km.xlsx')
    # df1 = pd.read_excel(r'C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Final_Output_Axis_26th.xlsx', sheet_name='Village_censuscode')
    
    df1 = pd.read_excel(f"{config.folder_path}\\Final_Output_Axis_26th.xlsx", sheet_name='Village_censuscode')
   
    
    # Convert 'censuscode2011' to string in both dataframes to ensure matching works correctly
    df1['censuscode2011'] = df1['censuscode2011'].astype(str)
    df2['censuscode2011'] = df2['censuscode2011'].astype(str)

    # Perform a left join on 'censuscode2011', including the 'Jun_23_Cat' column from df1
    merged_df = df2.merge(df1[['censuscode2011']], on='censuscode2011', how='left', indicator=True)
    # print(merged_df.columns)

    # Add 'Track-status' column based on the merge indicator
    merged_df['Track-status'] = merged_df['_merge'].apply(lambda x: 'Visited' if x == 'both' else 'Yet-To-Visit')
    # print(merged_df.columns)

    # Select only the columns you want to output
    output_columns = ['censuscode2011', 'Village', 'Pincode', 'district', 'state', 'tot_p_2011', 'no_hh_2011', 'lat_min_bound_centroid', 'long_min_bound_centroid', 'Final_Cat', 'Track-status','b_dist']
    final_output = merged_df[output_columns]
    # Rename columns
    new_column_names = {
        'censuscode2011': 'censuscode2011',
        'Village': 'Village',
        'Pincode': 'Pincode',
        'district': 'District',
        'state': 'State',
        'tot_p_2011': 'Population',
        'no_hh_2011': 'Households',
        'lat_min_bound_centroid': 'lat_min_bound_centroid',
        'long_min_bound_centroid': 'long_min_bound_centroid',
        'Final_Cat': 'Jun_23_Cat',
        'Track-status': 'Visited',
        'b_dist': 'Branch Distance'
    }

    final_output_renamed = final_output.rename(columns=new_column_names)

    # Reorder columns
    desired_column_order = [
        'censuscode2011',
        'Village',
        'Pincode',
        'District',
        'State',
        'Population',
        'Households',
        'lat_min_bound_centroid',
        'long_min_bound_centroid',
        'Jun_23_Cat',
        'Visited',
        'Branch Distance'
    ]

    final_output_reordered = final_output_renamed.reindex(columns=desired_column_order)
    output_path = f"{config.folder_path}\\villages\\{village}_Source_Map.xlsx"
    print(final_output_renamed)
    final_output_reordered.to_excel(output_path, index=False)
    # print(final_output_reordered.columns)
    # Save the result to a new Excel file
    # final_output_reordered.to_excel(rf'C:\Users\Teja\Desktop\Karthik\demo\py_outputs\villages\{village}_Source_Map.xlsx', index=False)
    # final_output_reordered.to_excel(config.folder_path +"\\villages"+ '\\{village}_Source_Map.xlsx', index=False)
    print("The output file with the specified columns has been saved successfully.")
    csv_file_paths = [
        r"C:\Users\Teja\Downloads\Combined_Village_Boundary_2023.csv"
        # r"C:\Users\Vijval\Downloads\KA_Village_Boundary_2023.csv",
        # r"C:\Users\Vijval\Downloads\BR_Village_Boundary_2023.csv",
    ]
    # "C:\Users\Teja\Downloads\Vijval\output_with_track_status.xlsx"
    # Load the Village_Details.xlsx file
    # village_details_path = rf"C:\Users\Teja\Downloads\Vijval\villages\{village}_Source_Map.xlsx"
    village_details_path = f"{config.folder_path}\\villages\\{village}_Source_Map.xlsx"
    village_details_df = pd.read_excel(village_details_path, dtype={'censuscode2011': str})
    # print(village_details_df['censuscode2011_right'].head())
    # Initialize an empty dictionary for the censuscode2011 to tru_2011 mapping
    census_to_tru_mapping = {}
    # print(village_details_df.columns)
    # Loop through each CSV file path
    for csv_file_path in csv_file_paths:
        # Load the current CSV file
        boundary_df = pd.read_csv(csv_file_path, dtype={'censuscode2011': str})
        # Convert and clean up the censuscode2011_right column
        boundary_df['censuscode2011'] = boundary_df['censuscode2011'].astype(str).str.split('.').str[0]
        # print(boundary_df['censuscode2011'].head())
        # Update the mapping dictionary with the current CSV's data
        # This assumes tru_2011 values are the same for any repeated censuscode2011 across files
        # If they might differ, you'll need to decide how to handle the discrepancies
        census_to_tru_mapping.update(boundary_df.set_index('censuscode2011')['tru_2011'].to_dict())

    # Check for unmatched census codes (optional, can be removed to speed up the process)
    unmatched_codes = set(village_details_df['censuscode2011']) - set(census_to_tru_mapping.keys())
    # if unmatched_codes:
        # print(f"Unmatched census codes: {unmatched_codes}")

        # Debug: print the columns before renaming and reindexing
    # print("Columns before renaming:", village_details_df.columns.tolist())

    # Map the 'tru_2011' values to the village details DataFrame using the 'censuscode2011' column
    village_details_df['tru_2011'] = village_details_df['censuscode2011'].map(census_to_tru_mapping)

    # Handle rows with missing 'tru_2011' data by setting a default value
    village_details_df['tru_2011'] = village_details_df['tru_2011'].fillna('Missing')

    # Remove the "Remark" column from the DataFrame if it exists
    if 'Remarks' in village_details_df.columns:
        village_details_df = village_details_df.drop(columns=['Remarks'])

    # Rename 'tru_2011' column to 'U/R'
    village_details_df.rename(columns={'tru_2011': 'U/R'}, inplace=True)
    print(village_details_df.columns)

    # Debug: print the columns after renaming
    # print("Columns after renaming:", village_details_df.columns.tolist())

    new_column_names = {
        'censuscode2011': 'censuscode2011',
        'Village': 'Village',
        'Pincode': 'Pincode',
        'district': 'District',
        'state': 'State',
        'tot_p_2011': 'Population',
        'no_hh_2011': 'Households',
        'U/R': 'U/R',
        'lat_min_bound_centroid': 'lat_min_bound_centroid',
        'long_min_bound_centroid': 'long_min_bound_centroid',
        'Final_Cat': 'Jun_23_Cat',
        'Track-status': 'Visited',
        'Branch Distance': 'Branch Distance'
    }

    # Ensure no duplicate columns after renaming
    final_output_renamed = village_details_df.rename(columns=new_column_names)

    # Debug: print the columns after final renaming
    print("Columns after final renaming:", final_output_renamed.columns.tolist())

    # Remove duplicate columns if they exist
    final_output_renamed = final_output_renamed.loc[:, ~final_output_renamed.columns.duplicated()]

    # Reorder columns
    desired_column_order = [
        'censuscode2011',
        'Village', 
        'Pincode', 
        'District', 
        'State', 
        'Population', 
        'Households', 
        'U/R',
        'lat_min_bound_centroid', 
        'long_min_bound_centroid', 
        'Jun_23_Cat', 
        'Visited',
        'Branch Distance'
    ]

    # Debug: check for duplicates in desired_column_order
    if len(desired_column_order) != len(set(desired_column_order)):
        print("Warning: There are duplicate columns in the desired_column_order")

    # Reindex DataFrame with the desired column order
    village_details_df = final_output_renamed.reindex(columns=desired_column_order)

    # Debug: print the final columns after reindexing
    # print("Columns after reindexing:", village_details_df.columns.tolist())

    # Fill blank cells in multiple columns with 0
    for column in columns_to_fill:
        village_details_df[column] = village_details_df[column].fillna(0).infer_objects(copy=False)

    # Save the updated DataFrame back to the Excel file
    village_details_df.to_excel(village_details_path, index=False, engine='openpyxl')
    print(village_details_df)

    print("The Village_Details.xlsx file has been updated with the 'U/R' column and reordered.")



    print(f"The Village_Details.xlsx file has been updated with tru_2011 data.")
    
        

    
    
for village in villages_ka:
    # Load the first Excel file (as per your description df1 should be the second file and df2 the first file)
    df2 = pd.read_excel(rf'C:\Users\Teja\Downloads\30km_Branches_Surroundings\KA_30km\{village}_30_km.xlsx')
    # df1 = pd.read_excel(r'C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Final_Output_Axis_26th.xlsx', sheet_name='Village_censuscode')
    
    df1 = pd.read_excel(f"{config.folder_path}\\Final_Output_Axis_26th.xlsx", sheet_name='Village_censuscode')
   
    
    # Convert 'censuscode2011' to string in both dataframes to ensure matching works correctly
    df1['censuscode2011'] = df1['censuscode2011'].astype(str)
    df2['censuscode2011'] = df2['censuscode2011'].astype(str)

    # Perform a left join on 'censuscode2011', including the 'Jun_23_Cat' column from df1
    merged_df = df2.merge(df1[['censuscode2011']], on='censuscode2011', how='left', indicator=True)
    # print(merged_df.columns)

    # Add 'Track-status' column based on the merge indicator
    merged_df['Track-status'] = merged_df['_merge'].apply(lambda x: 'Visited' if x == 'both' else 'Yet-To-Visit')
    # print(merged_df.columns)

    # Select only the columns you want to output
    output_columns = ['censuscode2011', 'Village', 'Pincode', 'district', 'state', 'tot_p_2011', 'no_hh_2011', 'lat_min_bound_centroid', 'long_min_bound_centroid', 'Final_Cat', 'Track-status','b_dist']
    final_output = merged_df[output_columns]
    # Rename columns
    new_column_names = {
        'censuscode2011': 'censuscode2011',
        'Village': 'Village',
        'Pincode': 'Pincode',
        'district': 'District',
        'state': 'State',
        'tot_p_2011': 'Population',
        'no_hh_2011': 'Households',
        'lat_min_bound_centroid': 'lat_min_bound_centroid',
        'long_min_bound_centroid': 'long_min_bound_centroid',
        'Final_Cat': 'Jun_23_Cat',
        'Track-status': 'Visited',
        'b_dist': 'Branch Distance'
    }

    final_output_renamed = final_output.rename(columns=new_column_names)

    # Reorder columns
    desired_column_order = [
        'censuscode2011',
        'Village',
        'Pincode',
        'District',
        'State',
        'Population',
        'Households',
        'lat_min_bound_centroid',
        'long_min_bound_centroid',
        'Jun_23_Cat',
        'Visited',
        'Branch Distance'
    ]

    final_output_reordered = final_output_renamed.reindex(columns=desired_column_order)
    output_path = f"{config.folder_path}\\villages\\{village}_Source_Map.xlsx"
    print(final_output_renamed)
    final_output_reordered.to_excel(output_path, index=False)
    # print(final_output_reordered.columns)
    # Save the result to a new Excel file
    # final_output_reordered.to_excel(rf'C:\Users\Teja\Desktop\Karthik\demo\py_outputs\villages\{village}_Source_Map.xlsx', index=False)
    # final_output_reordered.to_excel(config.folder_path +"\\villages"+ '\\{village}_Source_Map.xlsx', index=False)
    print("The output file with the specified columns has been saved successfully.")
    csv_file_paths = [
        r"C:\Users\Teja\Downloads\Combined_Village_Boundary_2023.csv"
        # r"C:\Users\Vijval\Downloads\KA_Village_Boundary_2023.csv",
        # r"C:\Users\Vijval\Downloads\BR_Village_Boundary_2023.csv",
    ]
    # "C:\Users\Teja\Downloads\Vijval\output_with_track_status.xlsx"
    # Load the Village_Details.xlsx file
    # village_details_path = rf"C:\Users\Teja\Downloads\Vijval\villages\{village}_Source_Map.xlsx"
    village_details_path = f"{config.folder_path}\\villages\\{village}_Source_Map.xlsx"
    village_details_df = pd.read_excel(village_details_path, dtype={'censuscode2011': str})
    # print(village_details_df['censuscode2011_right'].head())
    # Initialize an empty dictionary for the censuscode2011 to tru_2011 mapping
    census_to_tru_mapping = {}
    # print(village_details_df.columns)
    # Loop through each CSV file path
    for csv_file_path in csv_file_paths:
        # Load the current CSV file
        boundary_df = pd.read_csv(csv_file_path, dtype={'censuscode2011': str})
        # Convert and clean up the censuscode2011_right column
        boundary_df['censuscode2011'] = boundary_df['censuscode2011'].astype(str).str.split('.').str[0]
        # print(boundary_df['censuscode2011'].head())
        # Update the mapping dictionary with the current CSV's data
        # This assumes tru_2011 values are the same for any repeated censuscode2011 across files
        # If they might differ, you'll need to decide how to handle the discrepancies
        census_to_tru_mapping.update(boundary_df.set_index('censuscode2011')['tru_2011'].to_dict())

    # Check for unmatched census codes (optional, can be removed to speed up the process)
    unmatched_codes = set(village_details_df['censuscode2011']) - set(census_to_tru_mapping.keys())
    # if unmatched_codes:
        # print(f"Unmatched census codes: {unmatched_codes}")

        # Debug: print the columns before renaming and reindexing
    # print("Columns before renaming:", village_details_df.columns.tolist())

    # Map the 'tru_2011' values to the village details DataFrame using the 'censuscode2011' column
    village_details_df['tru_2011'] = village_details_df['censuscode2011'].map(census_to_tru_mapping)

    # Handle rows with missing 'tru_2011' data by setting a default value
    village_details_df['tru_2011'] = village_details_df['tru_2011'].fillna('Missing')

    # Remove the "Remark" column from the DataFrame if it exists
    if 'Remarks' in village_details_df.columns:
        village_details_df = village_details_df.drop(columns=['Remarks'])

    # Rename 'tru_2011' column to 'U/R'
    village_details_df.rename(columns={'tru_2011': 'U/R'}, inplace=True)
    print(village_details_df.columns)

    # Debug: print the columns after renaming
    # print("Columns after renaming:", village_details_df.columns.tolist())

    new_column_names = {
        'censuscode2011': 'censuscode2011',
        'Village': 'Village',
        'Pincode': 'Pincode',
        'district': 'District',
        'state': 'State',
        'tot_p_2011': 'Population',
        'no_hh_2011': 'Households',
        'U/R': 'U/R',
        'lat_min_bound_centroid': 'lat_min_bound_centroid',
        'long_min_bound_centroid': 'long_min_bound_centroid',
        'Final_Cat': 'Jun_23_Cat',
        'Track-status': 'Visited',
        'Branch Distance': 'Branch Distance'
    }

    # Ensure no duplicate columns after renaming
    final_output_renamed = village_details_df.rename(columns=new_column_names)

    # Debug: print the columns after final renaming
    print("Columns after final renaming:", final_output_renamed.columns.tolist())

    # Remove duplicate columns if they exist
    final_output_renamed = final_output_renamed.loc[:, ~final_output_renamed.columns.duplicated()]

    # Reorder columns
    desired_column_order = [
        'censuscode2011',
        'Village', 
        'Pincode', 
        'District', 
        'State', 
        'Population', 
        'Households', 
        'U/R',
        'lat_min_bound_centroid', 
        'long_min_bound_centroid', 
        'Jun_23_Cat', 
        'Visited',
        'Branch Distance'
    ]

    # Debug: check for duplicates in desired_column_order
    if len(desired_column_order) != len(set(desired_column_order)):
        print("Warning: There are duplicate columns in the desired_column_order")

    # Reindex DataFrame with the desired column order
    village_details_df = final_output_renamed.reindex(columns=desired_column_order)

    # Debug: print the final columns after reindexing
    # print("Columns after reindexing:", village_details_df.columns.tolist())

    # Fill blank cells in multiple columns with 0
    for column in columns_to_fill:
        village_details_df[column] = village_details_df[column].fillna(0).infer_objects(copy=False)

    # Save the updated DataFrame back to the Excel file
    village_details_df.to_excel(village_details_path, index=False, engine='openpyxl')
    print(village_details_df)

    print("The Village_Details.xlsx file has been updated with the 'U/R' column and reordered.")



    print(f"The Village_Details.xlsx file has been updated with tru_2011 data.")
    
        
    
for village in villages_br:
    # Load the first Excel file (as per your description df1 should be the second file and df2 the first file)
    df2 = pd.read_excel(rf'C:\Users\Teja\Downloads\30km_Branches_Surroundings\BR_30km\{village}_30_km.xlsx')
    # df1 = pd.read_excel(r'C:\Users\Teja\Desktop\Karthik\demo\py_outputs\Final_Output_Axis_26th.xlsx', sheet_name='Village_censuscode')
    
    df1 = pd.read_excel(f"{config.folder_path}\\Final_Output_Axis_26th.xlsx", sheet_name='Village_censuscode')
   
    
    # Convert 'censuscode2011' to string in both dataframes to ensure matching works correctly
    df1['censuscode2011'] = df1['censuscode2011'].astype(str)
    df2['censuscode2011'] = df2['censuscode2011'].astype(str)

    # Perform a left join on 'censuscode2011', including the 'Jun_23_Cat' column from df1
    merged_df = df2.merge(df1[['censuscode2011']], on='censuscode2011', how='left', indicator=True)
    # print(merged_df.columns)

    # Add 'Track-status' column based on the merge indicator
    merged_df['Track-status'] = merged_df['_merge'].apply(lambda x: 'Visited' if x == 'both' else 'Yet-To-Visit')
    # print(merged_df.columns)

    # Select only the columns you want to output
    output_columns = ['censuscode2011', 'Village', 'Pincode', 'district', 'state', 'tot_p_2011', 'no_hh_2011', 'lat_min_bound_centroid', 'long_min_bound_centroid', 'Final_Cat', 'Track-status','b_dist']
    final_output = merged_df[output_columns]
    # Rename columns
    new_column_names = {
        'censuscode2011': 'censuscode2011',
        'Village': 'Village',
        'Pincode': 'Pincode',
        'district': 'District',
        'state': 'State',
        'tot_p_2011': 'Population',
        'no_hh_2011': 'Households',
        'lat_min_bound_centroid': 'lat_min_bound_centroid',
        'long_min_bound_centroid': 'long_min_bound_centroid',
        'Final_Cat': 'Jun_23_Cat',
        'Track-status': 'Visited',
        'b_dist': 'Branch Distance'
    }

    final_output_renamed = final_output.rename(columns=new_column_names)

    # Reorder columns
    desired_column_order = [
        'censuscode2011',
        'Village',
        'Pincode',
        'District',
        'State',
        'Population',
        'Households',
        'lat_min_bound_centroid',
        'long_min_bound_centroid',
        'Jun_23_Cat',
        'Visited',
        'Branch Distance'
    ]

    final_output_reordered = final_output_renamed.reindex(columns=desired_column_order)
    output_path = f"{config.folder_path}\\villages\\{village}_Source_Map.xlsx"
    print(final_output_renamed)
    final_output_reordered.to_excel(output_path, index=False)
    # print(final_output_reordered.columns)
    # Save the result to a new Excel file
    # final_output_reordered.to_excel(rf'C:\Users\Teja\Desktop\Karthik\demo\py_outputs\villages\{village}_Source_Map.xlsx', index=False)
    # final_output_reordered.to_excel(config.folder_path +"\\villages"+ '\\{village}_Source_Map.xlsx', index=False)
    print("The output file with the specified columns has been saved successfully.")
    csv_file_paths = [
        r"C:\Users\Teja\Downloads\Combined_Village_Boundary_2023.csv"
        # r"C:\Users\Vijval\Downloads\KA_Village_Boundary_2023.csv",
        # r"C:\Users\Vijval\Downloads\BR_Village_Boundary_2023.csv",
    ]
    # "C:\Users\Teja\Downloads\Vijval\output_with_track_status.xlsx"
    # Load the Village_Details.xlsx file
    # village_details_path = rf"C:\Users\Teja\Downloads\Vijval\villages\{village}_Source_Map.xlsx"
    village_details_path = f"{config.folder_path}\\villages\\{village}_Source_Map.xlsx"
    village_details_df = pd.read_excel(village_details_path, dtype={'censuscode2011': str})
    # print(village_details_df['censuscode2011_right'].head())
    # Initialize an empty dictionary for the censuscode2011 to tru_2011 mapping
    census_to_tru_mapping = {}
    # print(village_details_df.columns)
    # Loop through each CSV file path
    for csv_file_path in csv_file_paths:
        # Load the current CSV file
        boundary_df = pd.read_csv(csv_file_path, dtype={'censuscode2011': str})
        # Convert and clean up the censuscode2011_right column
        boundary_df['censuscode2011'] = boundary_df['censuscode2011'].astype(str).str.split('.').str[0]
        # print(boundary_df['censuscode2011'].head())
        # Update the mapping dictionary with the current CSV's data
        # This assumes tru_2011 values are the same for any repeated censuscode2011 across files
        # If they might differ, you'll need to decide how to handle the discrepancies
        census_to_tru_mapping.update(boundary_df.set_index('censuscode2011')['tru_2011'].to_dict())

    # Check for unmatched census codes (optional, can be removed to speed up the process)
    unmatched_codes = set(village_details_df['censuscode2011']) - set(census_to_tru_mapping.keys())
    # if unmatched_codes:
        # print(f"Unmatched census codes: {unmatched_codes}")

        # Debug: print the columns before renaming and reindexing
    # print("Columns before renaming:", village_details_df.columns.tolist())

    # Map the 'tru_2011' values to the village details DataFrame using the 'censuscode2011' column
    village_details_df['tru_2011'] = village_details_df['censuscode2011'].map(census_to_tru_mapping)

    # Handle rows with missing 'tru_2011' data by setting a default value
    village_details_df['tru_2011'] = village_details_df['tru_2011'].fillna('Missing')

    # Remove the "Remark" column from the DataFrame if it exists
    if 'Remarks' in village_details_df.columns:
        village_details_df = village_details_df.drop(columns=['Remarks'])

    # Rename 'tru_2011' column to 'U/R'
    village_details_df.rename(columns={'tru_2011': 'U/R'}, inplace=True)
    print(village_details_df.columns)

    # Debug: print the columns after renaming
    # print("Columns after renaming:", village_details_df.columns.tolist())

    new_column_names = {
        'censuscode2011': 'censuscode2011',
        'Village': 'Village',
        'Pincode': 'Pincode',
        'district': 'District',
        'state': 'State',
        'tot_p_2011': 'Population',
        'no_hh_2011': 'Households',
        'U/R': 'U/R',
        'lat_min_bound_centroid': 'lat_min_bound_centroid',
        'long_min_bound_centroid': 'long_min_bound_centroid',
        'Final_Cat': 'Jun_23_Cat',
        'Track-status': 'Visited',
        'Branch Distance': 'Branch Distance'
    }

    # Ensure no duplicate columns after renaming
    final_output_renamed = village_details_df.rename(columns=new_column_names)

    # Debug: print the columns after final renaming
    print("Columns after final renaming:", final_output_renamed.columns.tolist())

    # Remove duplicate columns if they exist
    final_output_renamed = final_output_renamed.loc[:, ~final_output_renamed.columns.duplicated()]

    # Reorder columns
    desired_column_order = [
        'censuscode2011',
        'Village', 
        'Pincode', 
        'District', 
        'State', 
        'Population', 
        'Households', 
        'U/R',
        'lat_min_bound_centroid', 
        'long_min_bound_centroid', 
        'Jun_23_Cat', 
        'Visited',
        'Branch Distance'
    ]

    # Debug: check for duplicates in desired_column_order
    if len(desired_column_order) != len(set(desired_column_order)):
        print("Warning: There are duplicate columns in the desired_column_order")

    # Reindex DataFrame with the desired column order
    village_details_df = final_output_renamed.reindex(columns=desired_column_order)

    # Debug: print the final columns after reindexing
    # print("Columns after reindexing:", village_details_df.columns.tolist())

    # Fill blank cells in multiple columns with 0
    for column in columns_to_fill:
        village_details_df[column] = village_details_df[column].fillna(0).infer_objects(copy=False)

    # Save the updated DataFrame back to the Excel file
    village_details_df.to_excel(village_details_path, index=False, engine='openpyxl')
    print(village_details_df)

    print("The Village_Details.xlsx file has been updated with the 'U/R' column and reordered.")



    print(f"The Village_Details.xlsx file has been updated with tru_2011 data.")
    
        

    