import gspread
from oauth2client.service_account import ServiceAccountCredentials
from constants import CREDS_FILE_LOCATION, scope


def google_sheet_client():
    """Will return client which we will use in other functions to open sheet"""
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE_LOCATION, scope)

    client = gspread.authorize(creds)

    return client


def sheet_data(sheet_name, tab_name):
    """Function will return sheet data and sheet instance so that we can update sheet from other functions"""
    client = google_sheet_client()

    sheet = client.open(sheet_name).worksheet(tab_name)

    data = sheet.get_all_records()

    return data, sheet


