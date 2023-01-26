""" Attempt at using BeautifulSoup to parse websites with specific keywords. Some troubles in getting access to specific websites."""

import requests
from bs4 import BeautifulSoup
import argparse

def scrape_used_clothing(keywords, size, brand, shoe_size, price):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    URL = "https://www.grailed.com"
    params = {'keywords': keywords, 'size': size, 'brand': brand, 'shoe_size': shoe_size, 'price': price}
    r = requests.get(URL)#, params=params, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = []
    for item in soup.find_all('div', class_='item'):
        title = item.find('h3').text
        price = item.find('span', class_='price').text
        results.append({'title': title, 'price': price})
    return results

def main():
    # Create the parser
    parser = argparse.ArgumentParser()

    # Add arguments to the parser
    parser.add_argument('--keywords', required=True, help='Keywords to search for')
    parser.add_argument('--size', required=True, help='Size of the shoe')
    parser.add_argument('--brand', required=True, help='Brand of the shoe')
    parser.add_argument('--shoe_size', required=True, help='Shoe size')
    parser.add_argument('--price', required=True, help='Price of the shoe')

    # Parse the arguments
    args = parser.parse_args()

    # Extract the arguments
    keywords = args.keywords
    size = args.size
    brand = args.brand
    shoe_size = args.shoe_size
    price = args.price

    # You can now use the extracted arguments in your code
    results = scrape_used_clothing(keywords, size, brand, shoe_size, price)
    print(results)

if __name__ == '__main__':
    main() # ex: python webscraper.py --keywords mens --size small --brand nike --shoe_size 7.5 --price 100