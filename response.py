import random
import time
from pprint import pprint

import requests

from utils import get_response_product

url_head = 'https://goldapple.ru/front/api/catalog/products?categoryId=1000000007&cityId=dd8caeab-c685-4f2a-bf5f-550aca1bbc48&pageNumber='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': '',
    'DNT': '1',
    'x-app-version': '1.44.0',
    'traceparent': '00-423ceede237e7fe0e8dd61b4c1852ad8-97f1d62fa197dd3c-01',
    'x-gast': '36881857.23551748,36881857.23551748',
    'Content-Type': 'text/html; charset=utf-8',
}
count = 1
count_product = 1
check = ''
while count <= 5 and check == '':
    url = url_head + str(count)
    response = requests.get(url, headers=headers)
    pprint(response.json())
    data_json = response.json()
    if data_json['data']['count'] == 0:
        print('No products')
        check = 'no products'

    data = data_json['data']['products']
    # pprint(data[0])

    for item in data:
        # pprint(item)
        # value = random.random()
        # scaled_value = 1 + (value * (9 - 5))
        # print(scaled_value)
        # time.sleep(scaled_value)

        print('---------------------------------------------------------------------------------')
        print('count_product=', count_product)
        try:
            url = f'https://goldapple.ru{item["url"]}'
            name = item['name']
            brand = item['brand']
            price = item['price']['actual']['amount']
            rating = item['reviews']['rating'] if item.get('reviews') else None
            product = get_response_product(url)
            description = product['description']
            instructions = product['instructions']
            compound = product['compound']
            country = product['country']

            print('url=', url)
            print('name=', name)
            print('brand=', brand)
            print('price=', price)
            print('rating=', rating)
            print('description=', description)
            print('instructions=', instructions)
            print('compound=', compound)
            print('country=', country)
            count_product = count_product + 1
        except Exception as e:
            print(e)
    count = count + 1