import json
import re
import pandas as pd

def json_to_excel(json_file, excel_file):
    # Read JSON file into a Pandas DataFrame
    df = pd.read_json(json_file)

    # Write the DataFrame to an Excel file
    df.to_excel(excel_file, index=False)

def clean_json_file(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    cleaned_data = clean_json(data)

    with open(output_file, 'w') as file:
        json.dump(cleaned_data, file, indent=2)

def clean_json(data):
    cleaned_data = []
    for entry in data:
        contribution_text = entry.get("Contribution", "")
        cleaned_contribution = remove_time_related_strings(contribution_text)
        entry["Contribution"] = cleaned_contribution
        cleaned_data.append(entry)
    return cleaned_data

def remove_time_related_strings(contribution_text):
    time_patterns = [
        r"Contributed \d+ day[s]? ago by",
        r"Contributed about \d+ month[s]? ago by",
        r"Contributed \d+ month[s]? ago by ",
        r"Contributed about \d+ hours ago by",
        r"Contributed about \d+ hour[s]? ago by",
        r"Contributed \d+ hour[s]? ago by",
    ]

    time_regex = re.compile("|".join(time_patterns))
    cleaned_contribution = time_regex.sub("", contribution_text)
    return cleaned_contribution.strip()

if __name__ == "__main__":
    # Replace 'input.json' with the path to your input JSON file
    input_json_file = '../Output/Puppeteer_web_scraped_data.json'
    
    # Replace 'output_cleaned.json' with the desired output cleaned JSON file path
    output_json_file = '../Output/Puppeteer_web_cleaned.json'

    clean_json_file(input_json_file, output_json_file)
    print(f"Cleaning successful. Cleaned JSON file saved at {output_json_file}")


    clean_data = "../Output/output_cleaned.json"
    output_excel_file = '../Output/Puppeteer_Clean_Excel.xlsx'

    json_to_excel(clean_data, output_excel_file)
    print(f"Conversion successful. Excel file saved at {output_excel_file}")
