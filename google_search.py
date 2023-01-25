import json
from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup
import argparse

def get_requests():
    try: 
        URL = "https://poshmark.ca/"
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

def search_endpoints(args):
    # Define the search endpoint and the query
    endpoint = 'http://google.ca'
    query = args.keywords

    # Send the GET request
    response = requests.get(endpoint, params={'q': query})

    # Check the status code of the response
    if response.status_code == 200:
        parse_repsonse(response)
    else:
        print(f'Search failed with status code {response.status_code}')

def search_google_endpoints(args):
    # Define your API key and the query
    data = read_api_key()
    api_key = data.get("api_key")
    cx = data.get("cx")
    query = args.keywords

    # Define the endpoint and parameters
    endpoint = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cx,
        'q': query
    }

    # Send the GET request
    response = requests.get(endpoint, params=params)

    # Check the status code of the response
    if response.status_code == 200:
        # Extract the search results from the JSON response
        search_results = response.json()['items']
        for item in search_results:
            print(item['link'])
    else:
        print(f'Search failed with status code {response.status_code}')

def parse_repsonse(response):
    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the URLs from the search results
    links = [a['href'] for a in soup.select('a[href^="http"]')]

    # Print the URLs
    for link in links:
        print(link)

def read_api_key():
    with open("api_key.json", "r") as json_file:
        data = json.load(json_file)

    return data

if __name__ == '__main__':
    # Create the parser
    parser = argparse.ArgumentParser()

    # Add arguments to the parser
    parser.add_argument('--keywords', nargs='*', required=True, help='Keywords to search for')
    # parser.add_argument('--size', required=True, help='Size of the shoe')
    # parser.add_argument('--brand', required=True, help='Brand of the shoe')
    # parser.add_argument('--shoe_size', required=True, help='Shoe size')
    # parser.add_argument('--price', required=True, help='Price of the shoe')

    # Parse the arguments
    args = parser.parse_args()

    search_google_endpoints(args)