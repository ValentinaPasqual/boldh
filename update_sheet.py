import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import requests
import json

# Load credentials and authorize the Google Sheets API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('.github/workflows/boldh-412810-18a2c29d988c.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet using its ID
sheet_id = '1WKRWIkQ5qqr5caCEl5yaeHHuzDv_yF0fGpQs9dvBTgk'
document = client.open_by_key(sheet_id)

def agenda_json_builder(json_element):
    print(json_element)

    return json_element


def get_data_from_sheet(document, sheet, file_name):

    # Get data from the chosen sheet
    values = sheet.get_all_values()

    # Assuming your sheet has a header row, extract column names
    headers = values[0]

    # Create a list of dictionaries representing each row
    data = [dict(zip(headers, row)) for row in values[1:]]

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Convert DataFrame to list of dictionaries
    output_list = df.to_dict(orient='records')

    # Convert list to JSON format
    json_el = json.dumps(output_list, indent=2)

    if 'agenda' in file_name:
        json_el = agenda_json_builder(json_el)

    with open(f'content/{file_name}', 'w') as file:
        file.write(json_el)

news = document.get_worksheet(0)
get_data_from_sheet(document, news, 'news.json')

agenda = document.get_worksheet(1)
get_data_from_sheet(document, agenda, 'agenda.json')

# Clear existing data in the Google Sheet
#sheet.clear()

# Update the Google Sheet with the new data
#sheet.update([df.columns.values.tolist()] + df.values.tolist())
