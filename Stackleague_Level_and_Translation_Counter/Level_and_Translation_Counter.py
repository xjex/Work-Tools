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
file_path = "./dir1.xlsx"

# Install openpyxl if not already installed
try:
    import openpyxl
except ImportError:
    print("Installing openpyxl...")
    import subprocess
    subprocess.call(['pip', 'install', 'openpyxl'])

# Load the spreadsheet into a DataFrame
df = pd.read_excel(file_path)


level_counts_by_name = df.groupby(['Name', 'Levels']).size().unstack(fill_value=0)

# Count occurrences of each directionn

complete_translation_count = (df['Score'] == 1800.0).sum()
title = df["Name"].dropna().unique().tolist()
levels_count = df['Levels'].value_counts()
author_levels_count = df.groupby(['Author', 'Levels']).size().unstack(fill_value=0)
author_contributions = df.groupby(['Author','Levels']).size().to_frame('Contributions')
author_levels_count['Total'] = author_levels_count[['high', 'high mid', 'low','low mid']].sum(axis=1, numeric_only=True)
author_levels_count.loc['Total'] = author_levels_count.sum()
author_levels_count.loc['-'] = "-"
author_levels_count.loc['Complete Translation', 'Total'] = complete_translation_count
author_levels_count.loc['Complete Translation'] = author_levels_count.loc['Complete Translation'].fillna("-")


# Prepare the log content

log_content = f"------------Level Counts:\n{levels_count.to_string()}\nComplete Translation: {complete_translation_count}\nTotal Contribution: {len(title)}\n {author_levels_count} \n\n-------------------\n"
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
    log_file_path = 'Stackleague_Log_Report.txt'

     # Step 1: Enter name
    file_name = input("Enter Log Title name: ")
    save_log = False
    while True:
       
        
        # Step 2: Validate the name
        validation = input (f"is {Colors.GREEN}{file_name}{Colors.WHITE} correct? (y/n)").lower()

        if validation == 'y':

            log_content_with_name = f"-------------------\n{file_name}\nLevel Counts:\n{levels_count.to_string()}\nComplete Translation: {complete_translation_count}\nTotal Contribution: {len(title)}\n-------------------\n"
            with open(log_file_path, 'a') as log_file:
                log_file.write(log_content_with_name)
                Excel_path = 'Weekly Report.xlsx'
                author_levels_count.to_excel(Excel_path)
            os.system('cls' if os.name == 'nt' else 'clear')    
            print(Colors.GREEN)
            print(f"Log written to {log_file_path} , Excel file written to {Excel_path}")
            print(Colors.RESET)
            save_log = True
            break  # Exit the loop if the name is correct

        elif validation == 'n':
           
            file_name = input("Please Rename: ")
        else:
            
            print("Invalid input. Please enter 'y' or 'n'.")


else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colors.RED)
    print("Log not saved.")
    print(Colors.RESET)



