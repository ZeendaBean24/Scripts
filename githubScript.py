import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def get_repo_contents(repo_path, path='', token=''):
    """Fetches contents of a path in a GitHub repository."""
    api_url = f"https://api.github.com/repos/{repo_path}/contents/{path}"
    headers = {'Authorization': f'token {token}'}
    
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def list_all_contents(repo_path, path='', token='', level=1):
    """Recursively lists all folders, subfolders, and files in a GitHub repository in Markdown format."""
    contents = get_repo_contents(repo_path, path, token)
    if contents:
        for item in contents:
            if item['name'] not in ['.gitignore', '_template.cpp']:  # Skip specific files
                prefix = '#' * level
                if item['type'] == 'dir':
                    print(f"{prefix} {item['name']}")
                    list_all_contents(repo_path, item['path'], token, level + 1)
                else:
                    file_name = item['name']
                    if file_name.endswith('.cpp'):
                        file_path = f"https://github.com/{repo_path}/blob/master/{item['path']}"
                        print(f"- [x] [{file_name}]({file_path})")
                    else:
                        print(f"- [x] {file_name}")

# Fetch and print repository contents in Markdown format
token = os.getenv('GITHUB_TOKEN')
repo_path = 'ZeendaBean24/KitchenV2'

list_all_contents(repo_path, token=token)
