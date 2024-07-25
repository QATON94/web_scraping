import random
import time
from pprint import pprint

import requests

from services import Perfumery
from settings import url_head, headers
from utils import get_response_product


def get_response_products():
    count = 1
    count_product = 1
    check = ''
    data_perfumery = []
    while check == '':
        url = url_head + str(count)
        response = requests.get(url, headers=headers)
        value = random.random()
        scaled_value = 1 + (value * (9 - 5))
        print(scaled_value)
        time.sleep(scaled_value)
        # pprint(response.json())
        data_json = response.json()
        if not data_json['data']['products']:
            print('No products')
            check = 'no products'

        data = data_json['data']['products']
        # pprint(data[0])
        pause = 1
        for item in data:
            # pprint(item)

            print('---------------------------------------------------------------------------------')
            print('count_product=', count_product)
            try:
                url = f'https://goldapple.ru{item["url"]}'
                product = get_response_product(url)
                perfume = Perfumery(
                    url=url,
                    name=item['name'],
                    brand=item['brand'],
                    price=str(item['price']['actual']['amount']),
                    rating=str(item['reviews']['rating']) if item.get('reviews') else None,
                    description=product['description'],
                    instructions=product['instructions'],
                    compound=product['compound'],
                    country=product['country'],
                )
                print('url=', perfume.url)
                print('name=', perfume.name)
                print('brand=', perfume.brand)
                print('price=', perfume.price)
                print('rating=', perfume.rating)
                print('description=', perfume.description)
                print('instructions=', perfume.instructions)
                print('compound=', perfume.compound)
                print('country=', perfume.country)
                count_product = count_product + 1
                data_perfumery.append(perfume)
            except Exception as e:
                print(e)
            finally:
                if pause == 12:
                    value = random.random()
                    scaled_value = 1 + (value * (9 - 5))
                    print(scaled_value)
                    time.sleep(scaled_value)
                pause = pause + 1
        count = count + 1

    return data_perfumery
