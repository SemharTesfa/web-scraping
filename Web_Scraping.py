import pandas as pd
import requests
from bs4 import BeautifulSoup


class WebScraping:
    def __init__(self):
        self.carbonEmission = {}

    def get_data(self):
        r = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions")
        # print(r.status_code)
        webpage = BeautifulSoup(r.content, 'lxml')
        # print(webpage.prettify())
        table = webpage.select('table', class_='wikitable sortable jquery-tablesorter')[1]
        # print(table.prettify())

        for tr in table.find_all('tr')[5:]:
            tds = tr.find_all('td')
            self.carbonEmission[tds[0].text.strip()] = tds[4].text.strip('%')

        return self.carbonEmission

    def set_bug(self):
        data = self.get_data()
        for k, v in data.items():
            print(k, v)

# Testing
# s = WebScraping()
# s.get_data()
# s.set_bug()

