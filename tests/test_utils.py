import os
import re

import pytest
import requests
from bs4 import BeautifulSoup

from src.moduls import Perfumery
from src.settings import ROOT_PATH
from src.utils import get_response_product, get_description, get_text, save_csv, get_page_count


@pytest.fixture
def url():
    return 'https://goldapple.ru/19000247238-irresistible-very-floral'


@pytest.fixture
def get_response(url):
    response = requests.get(url)
    data = response.text
    data = BeautifulSoup(data, 'html.parser')
    return data


@pytest.fixture
def perfumery_product():
    product = Perfumery('url', 'name', 'brand', 'price', 'rating', 'description',
                        'instructions', 'compound', 'country')
    return product


def test_get_response_product(url):
    product = get_response_product(url)
    assert product == {'compound': 'Alcohol, parfum (fragrance), aqua (water), linalool, geraniol, '
                                   'citronellol, diethylamino hydroxybenzoyl hexyl benzoate, '
                                   'alpha-isomethyl ionone, limonene, methyl anthranilate, citral, '
                                   'tris(tetramethylhydroxypiperidinol) citrate, coumarin, ci 14700 '
                                   '(red 4), ci 17200 (red 33), ci 47005 (yellow 10), ci 60730 (ext. '
                                   'violet 2).',
                       'country': 'Франция ',
                       'description': 'Новый неотразимый древесно-цветочный женский аромат в сердце '
                                      'представлен интенсивным дуэтом пленительных цветов розы. '
                                      'Изысканный аромат Givenchy сочетает в себе Centifolia Rose и '
                                      'Rose Essential, чтобы выразить цветочные и очень женственные '
                                      'грани неотразимой фирменной розы. Белый букет из пудрового '
                                      'ириса, иланг-иланга и абсолюта жасмина самбак раскрывается, '
                                      'излучая солнечное сияние. Женский аромат удивляет своей '
                                      'дерзостью, раскрывая контраст между яркими гранями бутонов '
                                      'французской черной смородины и неожиданной свежестью аккорда '
                                      'кокосовой воды. Для создания стойкого шлейфа яркие древесные '
                                      'ноты кашмерана смешиваются с кедром, создавая глубоко '
                                      'звучащий мускусный аромат.',
                       'instructions': 'Нанесите аромат на запястья, шею и точки пульса.'}


def test_get_description(get_response):
    description_html = str(get_response.find_all(itemprop="description"))
    description_html = description_html.replace('\n', ' ')
    description_html = description_html.replace('<br/>', '')
    description = get_description(description_html)
    assert description == ('Новый неотразимый древесно-цветочный женский аромат в '
                           'сердце представлен интенсивным дуэтом пленительных цветов розы. '
                           'Изысканный аромат Givenchy сочетает в себе Centifolia Rose и '
                           'Rose Essential, чтобы выразить цветочные и очень женственные '
                           'грани неотразимой фирменной розы. Белый букет из пудрового '
                           'ириса, иланг-иланга и абсолюта жасмина самбак раскрывается, '
                           'излучая солнечное сияние. Женский аромат удивляет своей '
                           'дерзостью, раскрывая контраст между яркими гранями бутонов '
                           'французской черной смородины и неожиданной свежестью аккорда '
                           'кокосовой воды. Для создания стойкого шлейфа яркие древесные '
                           'ноты кашмерана смешиваются с кедром, создавая глубоко '
                           'звучащий мускусный аромат.'
                           )


def test_get_text(get_response):
    text_html = str(get_response.find_all(value=[re.compile('^Text')]))
    text_html = text_html.replace('\n', ' ')
    text_html = text_html.replace('<br/>', ' ')
    text_html = text_html.replace('<p>', ' ')
    text_html = text_html.replace('</p>', ' ')
    text = get_text(text_html)
    assert text == {"применение": 'Нанесите аромат на запястья, шею и точки пульса.',
                    "состав": 'Alcohol, parfum (fragrance), aqua (water), linalool, geraniol, '
                              'citronellol, diethylamino hydroxybenzoyl hexyl benzoate, '
                              'alpha-isomethyl ionone, limonene, methyl anthranilate, citral, '
                              'tris(tetramethylhydroxypiperidinol) citrate, coumarin, ci 14700 '
                              '(red 4), ci 17200 (red 33), ci 47005 (yellow 10), ci 60730 (ext. '
                              'violet 2).',
                    "страна происхождения": 'Франция '}


def test_save_csv(perfumery_product):
    save_csv([perfumery_product], 'test_perfumery.csv')
    assert os.path.isfile(ROOT_PATH.joinpath('data', 'test_perfumery.csv')) is True


def test_get_page_count():
    url_head = ('https://goldapple.ru/front/api/catalog/products?categoryId=1000000007&cityId='
                'dd8caeab-c685-4f2a-bf5f-550aca1bbc48&pageNumber=1')
    page_count = get_page_count(url_head)
    assert page_count == 496
