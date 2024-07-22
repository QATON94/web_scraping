import re

import requests
from bs4 import BeautifulSoup


def get_response_product(url):
    response = requests.get(url)
    data = response.text
    data = BeautifulSoup(data, 'html.parser')

    # Описание товара
    description_html = data.find_all(itemprop="description")
    description_html = str(description_html).replace('\n', ' ')
    description_html = str(description_html).replace('<br/>', '')
    print('-----------------------------------')
    print(description_html)
    description = get_description(description_html)
    print('-----------------------------------')
    print(description)

    # Название бренда и страны
    brand_html = data.find_all(value=[re.compile('^Brand')])
    brand_data = get_brand(brand_html)
    brand = brand_data[0]
    side = brand_data[1]

    # Text_1 Способ применения
    # Text_2 Состав
    # Text_3 Способ применения
    # Text_4 Страна происхождения и адрес

    application = data.find_all(value=[re.compile('^Text')])
    text = get_text(application)
    return description


def get_description(description):
    soup = re.findall('\"description\">(.*)</div>|\n', str(description))
    data = ''
    for i in soup:
        for j in i:
            if j != '':
                data += j
    return data


def get_brand(brand):
    soup = re.findall('>\n?(.*)<br/>?<br/>|\n?(.*)</div>|\n(.*)<br/>?<br/>|\n(.*?)\n', str(brand))
    data = []
    for i in soup:
        for j in i:
            word = re.findall('\w.*', j)
            if word:
                data.append(word[0])
    return data


def get_text(text_html):
    soup = re.findall('(Text_[1-5])|class=\"\w*\">(.*?)</div>', str(text_html))
    # print(soup)
    data = {}
    key = ''
    value = ''
    for i in soup:
        for j in i:
            # print(j)
            # print(re.findall('(Text_[1-5])', j))
            if "Text_" in j:
                key = j
                # print('key=', j)
            elif not "Text_" in j and j != '':
                value = j
                # print('value=', value)
            if key != '' and value != "":
                data[key] = value
    return data
