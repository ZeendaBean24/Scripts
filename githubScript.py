import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

token = os.getenv('GITHUB_TOKEN')
repo_path = 'ZeendaBean24/KitchenV2'

def get_repo_contents(repo_path, path='', token=''):
    """Fetches contents of a path in a GitHub repository."""
    api_url = f"https://api.github.com/repos/{repo_path}/contents/{path}"
    headers = {'Authorization': f'token {token}'}
    
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def list_all_contents(repo_path, path='', token='', indent=0):
    """Recursively lists all folders, subfolders, and files in a GitHub repository."""
    contents = get_repo_contents(repo_path, path, token)
    if contents:
        for item in contents:
            print(" " * indent + item['name'])
            if item['type'] == 'dir':  # If the item is a directory, recurse into it
                list_all_contents(repo_path, item['path'], token, indent + 2)

# def get_repo_info(repo_path):
#     """Fetches information about a GitHub repository."""
#     api_url = f"https://api.github.com/repos/{repo_path}"
#     token = os.getenv('GITHUB_TOKEN')
#     headers = {'Authorization': f'token {token}'}
    
#     response = requests.get(api_url, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return f"Error: {response.status_code}"

# Fetch and print repository information
# repo_info = get_repo_info(repo_path)
                
list_all_contents(repo_path, token=token)

