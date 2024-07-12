import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_facebook_profile(profile_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(profile_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        profile_info = {}
        profile_info['name'] = soup.find('h1', {'id': 'fb-timeline-cover-name'}).get_text(strip=True)
        # Add more fields as required
        
        return profile_info
    else:
        print("Failed to retrieve profile")
        return None

def save_data(data):
    if not os.path.exists('data'):
        os.makedirs('data')
    
    with open('data/profile_data.json', 'w') as f:
        json.dump(data, f, indent=4)

def main():
    with open('config.json', 'r') as f:
        config = json.load(f)
        
    profile_url = config['profile_url']
    profile_data = scrape_facebook_profile(profile_url)
    
    if profile_data:
        save_data(profile_data)

if __name__ == '__main__':
    main()
