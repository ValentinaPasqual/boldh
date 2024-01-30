import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import requests

# Load credentials and authorize the Google Sheets API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('.github/workflows/boldh-412810-18a2c29d988c.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet using its ID
sheet_id = '1WKRWIkQ5qqr5caCEl5yaeHHuzDv_yF0fGpQs9dvBTgk'
sheet = client.open_by_key(sheet_id).sheet1

# Function to fetch news data from a hypothetical API
def fetch_news():
    api_url = "https://api.example.com/news"  # Replace this with the actual API endpoint

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        news_data = response.json()  # Assuming the API returns JSON data

        # Extract relevant information from the API response
        formatted_news_data = []
        for article in news_data['articles']:
            formatted_article = {
                "Post type": article.get('post_type', 'No post type'),
                "Title": article.get('Title', 'No title')
            }
            formatted_news_data.append(formatted_article)

        return formatted_news_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return None

# Call the fetch_news function to get the actual news data
news_data = fetch_news()

# Convert data to DataFrame
df = pd.DataFrame(news_data)

# Clear existing data in the Google Sheet
sheet.clear()

# Update the Google Sheet with the new data
sheet.update([df.columns.values.tolist()] + df.values.tolist())
