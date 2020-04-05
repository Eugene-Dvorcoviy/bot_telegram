import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime

class Hryvnia:
    HRYVNIA_RUB = 'https://www.google.com/search?rlz=1C1VLSB_enRU725RU772&sxsrf=ALeKk00Fk4_WMw9g2y40QQF69twZtU8wEA%3A1585768681965&ei=6eiEXum3OpLA0PEPqcyR-AI&q=%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQAzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJ1D-A1jnHmCHIWgCcAB4AIABAIgBAJIBAJgBAKABAaoBB2d3cy13aXqwAQo&sclient=psy-ab&ved=0ahUKEwip0O_X-MfoAhUSIDQIHSlmBC8Q4dUDCAs&uact=5'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
        self.hryvnia_value = ' '
        self.current_hryvnia = float(self.get_currency_price())

    def get_currency_price(self):
        full_page = requests.get(self.HRYVNIA_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        return convert[0].text.replace(',', '.')

    def check_currency(self):
        pass