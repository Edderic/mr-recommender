import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def create_client():
    """
    Assumes that MR_RECOMMENDER_GOOGLE_SHEETS_CLIENT_SECRET_PATH exists. Search Lastpass
    for "DS Google Sheets".

    """
    scopes = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]


    secret_path_str = os.getenv("MR_RECOMMENDER_GOOGLE_SHEETS_CLIENT_SECRET_PATH")
    credentials = Credentials.from_service_account_file(
        secret_path_str,
        scopes=scopes
    )
    client = gspread.authorize(credentials)

    return client


def read_or_create_spreadsheet(spreadsheet_name, client, log, share_with=None):
    if share_with is None:
        share_with = os.getenv("MR_RECOMMENDER_EMAIL")
    try:
        overall_product_spreadsheet = client.open(spreadsheet_name)
        log.info("Read %s...", spreadsheet_name)
    except gspread.exceptions.SpreadsheetNotFound as e:
        # TODO: be more specific. Actually read the error. Do the following if
        # the open does not work because it does not exist yet
        overall_product_spreadsheet = client.create(spreadsheet_name)
        log.info("Created %s...", spreadsheet_name)
        overall_product_spreadsheet.share(share_with, perm_type='user', role='writer')
        log.info("Shared with %s...", share_with)

    return overall_product_spreadsheet

def read_or_create_worksheet(worksheet_name, spreadsheet, log):

    try:
        worksheet = spreadsheet.add_worksheet(title=worksheet_name, rows=100, cols=20)
        log.info("Added worksheet %s...", worksheet_name)
    except gspread.exceptions.APIError as e:
        # TODO: be more specific. Actually read the error. Do the following if
        # the worksheet already exists
        worksheet = spreadsheet.worksheet(worksheet_name)
        log.info("Read worksheet %s...", worksheet_name)

    return worksheet


def update_worksheet(worksheet_name, worksheet, data, log):
    log.info(f"Updating {worksheet_name}...")
    worksheet.update(data)
    log.info(f"Updated {worksheet_name}!")
