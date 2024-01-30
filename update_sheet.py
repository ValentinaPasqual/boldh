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

# Get all values from the sheet
values = sheet.get_all_values()

# Assuming your sheet has a header row, extract column names
headers = values[0]

# Create a list of dictionaries representing each row
news_data = [dict(zip(headers, row)) for row in values[1:]]

# Call the fetch_news function to get the actual news data
news_data = fetch_news()

# Convert data to DataFrame
df = pd.DataFrame(news_data)

# Clear existing data in the Google Sheet
sheet.clear()

# Update the Google Sheet with the new data
sheet.update([df.columns.values.tolist()] + df.values.tolist())
