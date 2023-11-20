import pandas as pd
import json

# Read JSON data from file
with open('../Output/Clean_API.json', 'r') as file:
    json_data = json.load(file)

# Convert the JSON data to a DataFrame
df = pd.json_normalize(json_data)

# Specify the output Excel file path
excel_file_path = '../Output/API_Data.xlsx'  # Replace with the desired output file path

# Write the DataFrame to an Excel file
df.to_excel(excel_file_path, index=False)

print(f'Data written to {excel_file_path}')
