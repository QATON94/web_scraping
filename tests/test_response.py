import json

import pytest

from src.response import *
from src.settings import TEST_TXT_PATH


@pytest.fixture
def data_page():
    with open(TEST_TXT_PATH, 'r', encoding='utf8') as f:
        data = json.load(f)
        return data['products']


def test_get_response_products():
    url_head = ('https://goldapple.ru/front/api/catalog/products?categoryId=1000000007&cityId='
                'dd8caeab-c685-4f2a-bf5f-550aca1bbc48&pageNumber=')
    page_count = 2
    response_product = get_response_products(url_head, page_count)
    assert isinstance(response_product, list)
    assert len(response_product) == 48


def test_response_product(data_page):
    data = response_product(data_page)
    assert data[0].name == 'Aqua Allegoria Mandarine Basilic'
