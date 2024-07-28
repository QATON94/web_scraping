import requests

from src.settings import headers
from src.moduls import Perfumery
from src.utils import get_response_product


def get_response_products(url_head: str, page_count: int) -> list[Perfumery]:
    """
    Функция получает с сайта все данные продуктов
    """
    data_perfumery = []
    for count in range(1, page_count + 1):
        url = url_head + str(count)
        response = requests.get(url, headers=headers)
        data_json = response.json()
        data_page = data_json["data"]["products"]
        data_products = response_product(data_page)
        data_perfumery.extend(data_products)
        print(f"Обработана страница {count}")
    return data_perfumery


def response_product(data: list[dict]) -> list[Perfumery]:
    data_perfumery = []
    for item in data:
        try:
            url = f'https://goldapple.ru{item["url"]}'
            product = get_response_product(url)
            perfume = Perfumery(
                url=url,
                name=item["name"],
                brand=item["brand"],
                price=str(item["price"]["actual"]["amount"]),
                rating=str(item["reviews"]["rating"]) if item.get("reviews") else None,
                description=product["description"],
                instructions=product["instructions"],
                compound=product["compound"],
                country=product["country"],
            )
            # print('url=', perfume.url)
            # print('name=', perfume.name)
            # print('brand=', perfume.brand)
            # print('price=', perfume.price)
            # print('rating=', perfume.rating)
            # print('description=', perfume.description)
            # print('instructions=', perfume.instructions)
            # print('compound=', perfume.compound)
            # print('country=', perfume.country)
            data_perfumery.append(perfume)
        except Exception as e:
            print(e)
    return data_perfumery
