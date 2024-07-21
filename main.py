import re
from pprint import pprint
from bs4 import BeautifulSoup
import requests

from utils import get_description, get_brand, get_text

# url = 'https://goldapple.ru/19000107891-aqua-allegoria-mandarine-basilic'
# url = 'https://goldapple.ru/83290100004-vetiver-d-haiti-au-the-vert'
url = 'https://goldapple.ru/19000191526-magnolia-bouquet'
# url = 'https://goldapple.ru/19000012381-enjoy'
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

response = requests.get(url)

data = response.text
# print(data)
print('---------------')
print('description')
data = BeautifulSoup(data, 'html.parser')
# description_html = data.find_all(itemprop="description")
# description = get_description(description_html)
# print(description)
# print('---------------')
brand_html = data.find_all(value=[re.compile('^Brand')])
# print(brand_html)
# brand_data = get_brand(brand_html)
# print('---------------')
# print('brand')
# print(brand_data)
# brand = brand_data[0]
# side = brand_data[1]
# print(brand)
# print(side)
application = data.find_all(value=[re.compile('^Text')])
print('---------------')
print('application')
print(application)

text = get_text(application)

print(text)
print('-----------------------------')


# pprint(data_2)
# description = bs.find('div', {'class': 'prT5M'})
# print(description)
# soup = re.findall(r'^"data":')
# pprint(bs.find_all("window.serverCache['productCard']={"))


