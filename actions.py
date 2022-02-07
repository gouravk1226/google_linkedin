import time
import secrets
from constants import SHEET_INFO, search_text, updated_data
from google_search import google_search
from google_sheet import sheet_data
import re


def get_index(row_data, column_name):
    index = 1
    for i in row_data:

        if i == column_name:
            return index
        index += 1


def get_linkedin():
    # google_linkedin = google_search('Cineplex')
    # for result in google_linkedin:
    #     print(result['link'])
    # quit()

    scrapped_data, sheet_instance = sheet_data(SHEET_INFO['sheet_name'], SHEET_INFO['tab_name'])
    print("Automation sheet -", scrapped_data)
    update_pos = 2

    for read_data in scrapped_data:
        # print(read_data)
        if read_data['Google LinkedIn Scrapped'] == 'No':

            print("Sheet opened -", read_data['Sheet Name'], "Tab opened -", read_data['Tab Name'])
            linkedin_data, linkedin_sheet_instance = sheet_data(read_data['Sheet Name'], read_data['Tab Name'])
            linkedin_column_index = get_index(linkedin_data[1], 'Company LinkedIn')
            print("LinkedIn column index is -", linkedin_column_index)
            i = 2
            for company in linkedin_data:
                print(company)
                if (company['Company LinkedIn']) == '':
                    try:
                        google_linkedin = google_search(company['Company'] + secrets.choice(search_text))

                        linkedin_link = get_link(google_linkedin)
                        print(linkedin_link)
                        time.sleep(2)

                    except Exception as error:
                        print(error)
                        continue

                else:
                    print("Already done")
                    i += 1
                    continue

                try:
                        linkedin_sheet_instance.update_cell(i, linkedin_column_index, linkedin_link)
                except Exception as error:
                    print(error)
                    i += 1
                    continue
                i += 1

            sheet_instance.update_cell(update_pos, get_index(read_data, 'Google LinkedIn Scrapped'), updated_data)
        else:
            update_pos += 1
            continue


def get_link(search_result):
    for result in search_result:
        if re.search('^h.......www[.]linkedin', result['link']) is not None or re.search('^h.........[.]linkedin', result['link']) is not None:
            return result['link']
    return "NA"
