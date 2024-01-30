import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Load credentials and authorize the Google Sheets API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/credentials.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet using its ID
sheet_id = 'your-google-sheet-id'
sheet = client.open_by_key(sheet_id).sheet1

# Fetch news data (replace this with your actual data fetching logic)
news_data = [
    {"Title": "News 1", "Date": "2024-01-30"},
    {"Title": "News 2", "Date": "2024-01-29"},
    # Add more rows as needed
]

# Convert data to DataFrame
df = pd.DataFrame(news_data)

# Clear existing data in the Google Sheet
sheet.clear()

# Update the Google Sheet with the new data
sheet.update([df.columns.values.tolist()] + df.values.tolist())
