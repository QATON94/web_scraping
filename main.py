import re
from pprint import pprint
from bs4 import BeautifulSoup
import requests

from utils import get_text

url = 'https://goldapple.ru/19000139406-eau-de-parfum-e-motion'
response = requests.get(url)
data = response.text
data = BeautifulSoup(data, 'html.parser')
instructions = str(data.find_all(value=[re.compile('^Text')]))
instructions = instructions.replace('\n', ' ')
instructions = instructions.replace('<br/>', ' ')
print(instructions)
text = get_text(instructions)
print(text)