import requests
from bs4 import BeautifulSoup

link = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'

feedback = requests.get(link).text
soup = BeautifulSoup(feedback, 'lxml')
blocks = soup.find_all('div', class_='thumbnail')

# Iterate through the blocks
for idx, block in enumerate(blocks, start=1):
    title = block.find('a', class_='title')
    price = block.find('h4', class_='pull-right price')
    description = block.find('p', class_='description')
    if title:
        print(
            f"Laptop {idx}: {title.text}\nЦіна: {price.text}\nОпис: {description.text}")
