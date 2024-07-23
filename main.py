import pickle
import re
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import csv

from response import get_response_products
from services import Perfumery
from utils import save_csv


def main() -> None:
    data_perfumes = get_response_products()
    # data_perfumes = [Perfumery(url='https://goldapple.ru/82082400001-tamarindo', name='TAMARINDO',
    #                            brand='MEMO Paris',
    #                            price=25905,
    #                            rating=None,
    #                            description='Подобно экзотическому цветку, аромат Memo Tamarindo появился на свет в начале 2018 года и раскрасил морозные дни в яркие радужные цвета. В нем чувствуется экспрессия и особенный ритм, позволивший его создателям провести параллель с танцем под звуки там-тамов на небольшой поляне среди пышной южной зелени.  Воздух пронизан чистыми и свежими солнечными тонами ананаса: его соло  возносится над опьяняющим дымным сплетением нот пачули и бензоина. Плотный туман клубится вокруг ног, и каждое па взбивает его, словно пушистую перину. Мягкая подсветка сливочных тонов ванили придает всей композиции футуристический характер: кусочек джунглей и вечного лета среди бесконечной, космических масштабов, заснеженной равнины манит к себе  подобно миражу в пустыне. Страна чудес – Тамариндо.',
    #                            instructions=None,
    #                            compound=None,
    #                            country='Россия', )]
    save_csv(data_perfumes)


if __name__ == '__main__':
    main()
