import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
import requests
import xml.etree.ElementTree as ET

from sales.exceptions import CBException

CREDENTIALS_FILE: str = 'cred.json'
DOLLAR_ID: str = "R01235"


spreadsheet_id: str = "18MU3oHVREe5VH0jZEM-wLAtbjVjYsvbbWn0Fkle4WqY"
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive']
)

httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)


def get_all_values() -> tuple:
    """ Get all values from google sheet

    Args:

    Returns:
        Info about all orders
    """
    info = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range="B2:D",
        majorDimension="ROWS"
    ).execute()

    return info.get("values")


def get_current_dollar_course() -> int:
    """Get current course of dollar from cbr

    Returns:
        how many rubles costs one dollar raises error if can not connect to cbr
    """
    url: str = "https://www.cbr.ru/scripts/XML_daily.asp?"
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

    else:
        raise CBException("Status code not equal to 200. Something goes wrong!")

    tree = ET.fromstring(content)

    valutes = tree.findall("Valute")

    for valute in valutes:

        if valute.get("ID") == DOLLAR_ID:
            one_dollar = int(valute.find("Value").text.split(",")[0])

            return one_dollar


def get_deleted_sales(new_sale_list: tuple, old_sale_list: list) -> list:
    """Return deletes sales

    Args:
        new_sale_list: new sale list got with api
        old_sale_list: old order list from db

    Returns:
        orders that dont exist in new sale list
    """
    deleted_sales_tuple = tuple(sale[0] for sale in old_sale_list if sale[0] not in new_sale_list)
    print(deleted_sales_tuple)

    deleted_sales = list()

    for sale in old_sale_list:
        if sale[0] not in new_sale_list:
            deleted_sales.append(sale[0])

    return deleted_sales
