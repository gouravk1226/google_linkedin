path = "/home/casper/Downloads/chromedriver_linux64/chromedriver"

SHEET_INFO = {
    'sheet_name': 'Scrap Companies Linkedin URL',
    'tab_name': 'Missing LinkedIn Automation',
}

CREDS_FILE_LOCATION = "creds.json"

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

search_text = [' linkedin profile', 'linkedin', 'profile on linkedin',]

updated_data = 'Yes'