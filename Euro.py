import requests
from bs4 import BeautifulSoup


class Euro:
    EURO_RUB = 'https://www.google.com/search?newwindow=1&rlz=1C1VLSB_enRU725RU772&sxsrf=ALeKk03TSWxu1WWL5kOOKuhjSshdf2fqtQ%3A1586976625104&ei=cVeXXu38BcnQ6QTj1bKgBg&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%83%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQARgAMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKOgQIABBHOgYIABAHEB5KEQgXEg0xMC0xODZnMTY4ZzE2SgwIGBIIMTAtMWcxZzJQwf0MWPmEDWDEkQ1oAHACeAGAAewFiAGACpIBBzAuMy42LTGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
        self.euro_value = ' '
        self.current_euro = float(self.get_currency_price())

    def get_currency_price(self):
        full_page = requests.get(self.EURO_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        return convert[0].text.replace(',', '.')