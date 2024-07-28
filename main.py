from src.response import get_response_products
from src.settings import url_head
from src.utils import save_csv, get_page_count


def main() -> None:
    page_count = get_page_count(url_head+str(1))
    data_main_page_perfumery = get_response_products(url_head, page_count)
    save_csv(data_main_page_perfumery)

if __name__ == '__main__':
    main()
