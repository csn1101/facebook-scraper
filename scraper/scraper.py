import requests
from bs4 import BeautifulSoup
import json

def scrape_facebook_profile(profile_url):
    # Send a GET request to the profile URL
    response = requests.get(profile_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example selectors (update these based on actual HTML structure)
        name_element = soup.find('h1', class_='profile-name')
        followers_element = soup.find('span', class_='followers-count')

        # Extract text safely
        name = name_element.get_text() if name_element else "Name not found"
        followers = followers_element.get_text() if followers_element else "Followers count not found"

        # Prepare data to return
        scraped_data = {
            "name": name,
            "followers": followers,
            "profile_url": profile_url
        }
        
        return scraped_data
    else:
        print(f"Failed to retrieve profile. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    url = "https://www.example.com/someprofile"  # Replace with actual profile URL
    data = scrape_facebook_profile(url)
    
    if data:
        print("Scraped Data:", data)
        
        # Save to a JSON file
        with open('output.json', 'w') as f:
            json.dump(data, f, indent=4)
