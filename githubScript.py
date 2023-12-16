import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def get_repo_info(repo_path):
    """Fetches information about a GitHub repository."""
    api_url = f"https://api.github.com/repos/{repo_path}"
    token = os.getenv('GITHUB_TOKEN')
    headers = {'Authorization': f'token {token}'}
    
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

# Replace with the target repository
repo_path = 'ZeendaBean24/Scripts'

# Fetch and print repository information
repo_info = get_repo_info(repo_path)
print(repo_info)