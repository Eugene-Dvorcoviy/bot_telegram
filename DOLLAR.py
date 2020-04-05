import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime


class Dollar:
    DOLLAR_RUB = 'https://www.google.com/search?rlz=1C1VLSB_enRU725RU772&sxsrf=ALeKk02twJQ4QxMOgb3MfN1h6Z1VYBTulQ%3A1585752981080&ei=lauEXsO7BIu-tQb0oJfABQ&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQAzIKCAAQgwEQRhCCAjIFCAAQgwEyAggAMgIIADIFCAAQgwEyAggAMgIIADICCAAyAggAMgIIADoHCAAQgwEQQzoECAAQQ1CZDFjjLWD4MGgCcAB4A4AByguIAYopkgELMy00LjQuMS4wLjGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwiD2o2ZvsfoAhULX80KHXTQBVgQ4dUDCAs&uact=5'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
        self.dollor_value = 78.5
        self.current_dollor = float(self.get_currency_price())

    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        return convert[0].text.replace(',', '.')

    def check_currency(self):
        if self.current_dollor > self.dollor_value:
            return "Курс долора к рублю: {}. \n Рубль опять падает.".format(self.current_dollor)
        elif self.current_dollor > self.dollor_value:
            return "Курс долора к рублю: {}. \n Рубль растет.".format(self.current_dollor)
        else:
            return "Курс долора к рублю: {}. \n Ничего не изменилось.".format(self.current_dollor)



