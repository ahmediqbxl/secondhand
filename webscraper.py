import requests
from bs4 import BeautifulSoup

def scrape_used_clothing(keywords, size, brand, shoe_size, price):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    URL = "https://www.example.com/used-clothing?"
    params = {'keywords': keywords, 'size': size, 'brand': brand, 'shoe_size': shoe_size, 'price': price}
    r = requests.get(URL, params=params, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = []
    for item in soup.find_all('div', class_='item'):
        title = item.find('h3').text
        price = item.find('span', class_='price').text
        results.append({'title': title, 'price': price})
    return results