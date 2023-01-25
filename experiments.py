from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup
import argparse

def get_requests():
    try: 
        URL = "https://www.nike.com/ca/men?sitelink=ENBrandCoreE1&cp=29728419214_search_%7cnike%7c10628221437%7c106336396713%7ce%7cc%7cEN%7cpure%7c452151650142&ds_rl=1252249&gclid=Cj0KCQiAt66eBhCnARIsAKf3ZNGDAFg5rkAxCjpKAJlblJjDwHzRqvILEWe0vUzmKWFY-aSBDuGTXJQaAmKyEALw_wcB&gclsrc=aw.ds"
        response = requests.get(URL, params={})
        print(response.status_code)
    # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

        return response

if __name__ == '__main__':
    response = get_requests()
    print(response.text)