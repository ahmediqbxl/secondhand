""" Using Google Programmable Search Engine to search for keywords and return links."""

import json
from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup

class GPSE():
    def __init__(self, args) -> None:
        self.args = args
        
    def get_requests(self):
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

    def search_endpoints(self):
        # Define the search endpoint and the query
        endpoint = 'http://google.ca'
        query = self.args.keywords

        # Send the GET request
        response = requests.get(endpoint, params={'q': query})

        # Check the status code of the response
        if response.status_code == 200:
            self.parse_repsonse(response)
        else:
            print(f'Search failed with status code {response.status_code}')

    def search_google_endpoints(self):
        # Define your API key and the query
        data = self.read_api_key()
        api_key = data.get("api_key")
        cx = data.get("cx")
        query = self.args.keywords

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

    def parse_repsonse(self, response):
        # Parse the HTML response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the URLs from the search results
        links = [a['href'] for a in soup.select('a[href^="http"]')]

        # Print the URLs
        for link in links:
            print(link)

    def read_api_key(self):
        with open("api_key.json", "r") as json_file:
            data = json.load(json_file)

        return data