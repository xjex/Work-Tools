import pandas as pd
import os

#CLI Colors
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

# Replace 'your_file.xlsx' with the actual filename of your spreadsheet
file_path = 'dir.xlsx'

# Install openpyxl if not already installed
try:
    import openpyxl
except ImportError:
    print("Installing openpyxl...")
    import subprocess
    subprocess.call(['pip', 'install', 'openpyxl'])

# Load the spreadsheet into a DataFrame
df = pd.read_excel(file_path)

# Count occurrences of each direction
levels_count = df['Levels'].value_counts()
complete_translation_count = (df['Score'] == 1800.0).sum()
title = df["Name"].dropna().unique().tolist()


# Prepare the log content
log_content = f"Level Counts:\n{levels_count.to_string()}\nComplete Translation: {complete_translation_count}\nTotal Contribution: {len(title)}\n-------------------\n"
#clear console
os.system('cls' if os.name == 'nt' else 'clear')
# Display the counts
print(log_content)



user_input = input("Do you want to save the log? (y/n): ")

# Validate the user input
while user_input.lower() not in ('y', 'n'):

    
    #clear console
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Display the counts
    print(f"{Colors.RESET}{log_content}") 
   
    # Display the error message
    print(f"{Colors.RED}Invalid input. Please enter 'y' or 'n'.") 
    user_input = input(f"{Colors.GREEN}Do you want to save the log? (y/n): ")


if user_input.lower() == 'y':
    # Write the log to a text file
    log_file_path = 'Log.txt'
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_content)
    os.system('cls' if os.name == 'nt' else 'clear')    
    print(Colors.GREEN)
    print(f"Log written to {log_file_path}")
    print(Colors.RESET)
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colors.RED)
    print("Log not saved.")
    print(Colors.RESET)



