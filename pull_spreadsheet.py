import logging
import pandas as pd

from sheets import read_or_create_spreadsheet, read_or_create_worksheet, create_client, update_worksheet


if __name__ == '__main__':
    log = logging

    sheets_client = create_client()

    spreadsheet_name = 'FTtP'
    spreadsheet = read_or_create_spreadsheet(
        spreadsheet_name,
        client=sheets_client,
        log=log,
    )

#
    worksheet_name = 'Main'
    worksheet = read_or_create_worksheet(
        worksheet_name=worksheet_name,
        spreadsheet=spreadsheet,
        log=log
    )

    crash_test_data = pd.DataFrame(worksheet.get_all_records())
    import pdb; pdb.set_trace()

    # TODO: add code to pull data from forklift to get Overall North Star KPIs for Product

