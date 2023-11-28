import requests
import pandas as pd
import json
import datetime
import os

current_datetime = datetime.datetime.now()
date = current_datetime.strftime("%Y-%m-%d")
folder_path = f'../Output/stackdata/{date}/'
os.makedirs(folder_path, exist_ok=True)
url = "https://www.stackleague.com/api/custom_problems?status=pending"


headers = {
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
    " (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.stackleague.com/admin/user-contributions",
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdGFja3RyZWtfYWNjb3VudCIsImV4cCI6MTcwMjk2ODI1MywiaWF0IjoxNzAwNTQ5MDUzLCJpc3MiOiJzdGFja3RyZWtfYWNjb3VudCIsImp0aSI6IjYzYjMyZGUwLWJhODMtNDU3MS05NDdmLTE1MDRmYWEzMDM4OCIsIm5iZiI6MTcwMDU0OTA1Miwic3ViIjoiNjI4MzQiLCJ0eXAiOiJhY2Nlc3MifQ.hX7PVKv9HsXJ1gND4g4F5yO6aFaTbQhIUMrGUnbtJ-_A6yTE_2jnPnssvI9IFYjAIr1F1qBoSc1u7P2fTMlRUw",
    "Cookie": "_hjFirstSeen=1; _hjIncludedInSessionSample_3466922=1; _hjSession_3466922=eyJpZCI6IjRhMjZiOWNjLTMwMWEtNDQwOC04MjAzLWM0OWZiNWRjYjkxNCIsImNyZWF0ZWQiOjE3MDA1NDkwNDYzMTksImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=; _hjSessionUser_3466922=eyJpZCI6ImJkNzcwNDBhLTgxOTUtNTQ0Yi05OGE0LTkyZjhmZWJhZjljYyIsImNyZWF0ZWQiOjE3MDA1NDkwNDYzMTgsImV4aXN0aW5nIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; _ga=GA1.1.484857375.1700549047; welcome-notif=false; stacktrek-token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdGFja3RyZWtfYWNjb3VudCIsImV4cCI6MTcwMjk2ODI1MywiaWF0IjoxNzAwNTQ5MDUzLCJpc3MiOiJzdGFja3RyZWtfYWNjb3VudCIsImp0aSI6IjYzYjMyZGUwLWJhODMtNDU3MS05NDdmLTE1MDRmYWEzMDM4OCIsIm5iZiI6MTcwMDU0OTA1Miwic3ViIjoiNjI4MzQiLCJ0eXAiOiJhY2Nlc3MifQ.hX7PVKv9HsXJ1gND4g4F5yO6aFaTbQhIUMrGUnbtJ-_A6yTE_2jnPnssvI9IFYjAIr1F1qBoSc1u7P2fTMlRUw; _ga_1PY4BQGEMP=GS1.1.1700549047.1.1.1700549170.59.0.0"

    # Add any other headers as needed
}

def Response():
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        #print("POST request successful")
        #print("Response content:", response.text)
        # Convert the JSON response to a dictionary
        
        with open(f"{folder_path}Scraper_GetRequest.json", "w") as json_file:
            json.dump(response.json(), json_file, indent=4)

    else:
        print("POST request failed. Status code:", response.status_code)
        print("Response content:", response.text)

    

Response()

# Read the JSON file
json_file_path = f"{folder_path}Scraper_GetRequest.json"  # Replace with the actual path to your JSON file
with open(json_file_path, "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Function to extract the desired information
def extract_data(problem):
    return {
        "id": problem["id"],
        "name": problem["name"],
        "status": problem["status"],
        "author": {
            "id": problem["author"]["id"],
            "email": problem["author"]["email"],
            "firstName": problem["author"]["firstName"],
            "lastName": problem["author"]["lastName"],
        },
        "comments": problem["comments"],
        "Language": [test["language"]["name"] for test in problem["tests"]],
        "score": [score["points"] for score in problem["score"]],
        "authorId": problem["authorId"],
        "insertedAt": problem["insertedAt"],
        "updatedAt": problem["updatedAt"],
        "skillTags": problem["skillTags"],
        "skillOverView": list(problem["skillTags"].items()),
    }


# Extract data for each problem in the 'data' array
extracted_data = list(map(extract_data, data["data"]))

# Write the extracted data to a new JSON file
output_file_path = f"{folder_path}Scraper_Clean_API.json"  # Replace with the desired output path
with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(extracted_data, output_file, indent=2)

print(f"Extracted data written to {output_file_path}")


# JSON to Excel
# Read JSON data from file
with open(f'{folder_path}Scraper_Clean_API.json', 'r') as file:
    json_data = json.load(file)

# Convert the JSON data to a DataFrame
df = pd.json_normalize(json_data)

# Specify the output Excel file path
excel_file_path = f'{folder_path}Scraper_API_Data.xlsx'  # Replace with the desired output file path

# Write the DataFrame to an Excel file
df.to_excel(excel_file_path, index=False)

print(f'Data written to {excel_file_path}')