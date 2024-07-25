import csv
import re

import requests
from bs4 import BeautifulSoup

from services import Perfumery


def get_response_product(url: str) -> dict[str, str | None]:
    """
    Функция делает запрос по url продукта
    :param url:
    :return: список: описание, способ применения, состав, адрес
    """
    response = requests.get(url)
    data = response.text
    data = BeautifulSoup(data, 'html.parser')
    product = {'description': '', 'applications': '', 'compound': '', 'address': ''}
    # Описание товара
    description_html = str(data.find_all(itemprop="description"))
    description_html = description_html.replace('\n', ' ')
    description_html = description_html.replace('<br/>', '')
    description = get_description(description_html)

    # Text_? Способ применения, Состав, О бренде, страна происхождения и адрес

    instructions = str(data.find_all(value=[re.compile('^Text')]))
    instructions = instructions.replace('\n', ' ')
    instructions = instructions.replace('<br/>', ' ')
    # print(instructions)
    text = get_text(instructions)

    product['description'] = description
    product['instructions'] = text['применение']
    product['compound'] = text['состав']
    product['country'] = text['страна происхождения']

    return product


def get_description(description: str) -> str:
    """
    Получает описание продукта из строки
    """
    soup = re.findall('\"description\">(.*)</div>|\n', description)
    data = ''
    for i in soup:
        for j in i:
            if j != '':
                data += j
    return data


def get_text(text_html: str) -> dict[str, str | None]:
    """
    Получает применение, состав, страну происхождения из строки
    """
    soup = re.findall('(состав)\" value=\"Text_[1-5]\"><!-- --> <!-- --> <div class=\"\w*\">(.*?)</div>|'
                      '(страна происхождения) (\w*? ? \w*) (изготовитель)?(</div>)?|'
                      '(применение)\" value=\"Text_[1-5]\"><!-- --> <!-- --> <div class=\"\w*\">(.*?)</div>',
                      text_html)
    # print(soup)
    data = {"применение": None, "состав": None, "страна происхождения": None}

    for i in soup:
        for j in range(len(i)):
            if "применение" in i[j]:
                data[i[j]] = i[j + 1]
            elif "состав" in i[j]:
                data[i[j]] = i[j + 1]
            elif "страна происхождения" in i[j]:
                data[i[j]] = i[j + 1]
    return data


def save_csv(data: list[Perfumery]) -> None:
    head = ['url', 'name', 'brand', 'price', 'rating', 'description', 'instructions', 'compound', 'country']
    with open('data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=head, delimiter=';')
        writer.writeheader()
        for row in data:
            writer.writerow({'url': row.url, 'name': row.name, 'brand': row.brand, 'price': row.price, 'rating': row.rating,
                             'description': row.description, 'instructions': row.instructions, 'compound': row.compound,
                             'country': row.country})
