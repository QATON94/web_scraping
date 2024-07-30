from pathlib import Path

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/126.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
              "image/apng,*/*;q=0.8,application/",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "",
    "DNT": "1",
    "x-app-version": "1.44.0",
    "traceparent": "00-423ceede237e7fe0e8dd61b4c1852ad8-97f1d62fa197dd3c-01",
    "x-gast": "36881857.23551748,36881857.23551748",
    "Content-Type": "text/html; charset=utf-8",
}

url_head = ("https://goldapple.ru/front/api/catalog/products?"
            "categoryId=1000000007&cityId=dd8caeab-c685-4f2a-bf5f-550aca1bbc48&pageNumber=")

ROOT_PATH = Path(__file__).parent.parent
PRODUCTS_PATH = ROOT_PATH.joinpath("data", "perfumery.csv")
TEST_TXT_PATH = ROOT_PATH.joinpath("tests", "test_page.json")

count_product = 1
