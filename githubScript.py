import requests
from dotenv import load_dotenv
import os
import pyperclip  # Import the pyperclip library

# Load environment variables
load_dotenv()

def get_repo_contents(repo_path, path='', token=''):
    # Fetches contents of a path in a GitHub repository.
    api_url = f"https://api.github.com/repos/{repo_path}/contents/{path}"
    headers = {'Authorization': f'token {token}'}

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def list_all_contents(repo_path, path='', token='', level=1):
    # Recursively lists all folders, subfolders, and files in a GitHub repository in Markdown format.
    contents = get_repo_contents(repo_path, path, token)
    output = []  # Create a list to store the output
    if contents:
        for item in contents:
            if item['name'] not in ['.gitignore', '_template.cpp', 'README.md']:  # Skip specific files
                prefix = '#' * level
                if item['type'] == 'dir':
                    output.append(f"{prefix} {item['name']}")
                    output.extend(list_all_contents(repo_path, item['path'], token, level + 1))
                else:
                    file_name = item['name']
                    if file_name.endswith('.cpp'):
                        file_path = f"https://github.com/{repo_path}/blob/master/{item['path']}"
                        output.append(f"- [x] [{file_name}]({file_path})")
                    else:
                        output.append(f"- [x] {file_name}")
    return output  # Return the output as a list

# Fetch repository contents in Markdown format
token = os.getenv('GITHUB_TOKEN')
# Change this to whatever path/repository it needs to fetch it from
repo_path = 'ZeendaBean24/KitchenV2'

output_list = list_all_contents(repo_path, token=token)

# Join the output list into a string with newlines
output_text = '\n'.join(output_list)

# Copy the output to the clipboard
pyperclip.copy(output_text)
print("Markdown content has been copied to the clipboard.")
print("REMINDER: GIT PULL RIGHT AFTER COMMITTING THE CHANGES ON GITHUB")