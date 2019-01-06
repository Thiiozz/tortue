# coding: utf8

import requests
from bs4 import BeautifulSoup


class WikiScrapper:
    def __init__(self):
        self.TARGET = 'https://fr.wikipedia.org/wiki/Spécial:Page_au_hasard'

    def get_random_wki_page(self):
        output = ''

        random_wiki_page_url = self.TARGET
        r = requests.get(random_wiki_page_url)

        if r.status_code == 200:
            output = r.text

        return output

    def extract_data_from_random_page(self):
        page = self.get_random_wki_page()
        soup = BeautifulSoup(page, 'html.parser')

        out = {
            'title': extract_title_from_data(soup),
            'text': extract_text_from_data(soup)
        }

        return out


def extract_title_from_data(soup):
    title = ""

    h1 = soup.find('h1', {'id': 'firstHeading'})

    if h1 is not None:
        title = h1.text

    return title


def extract_text_from_data(soup):
    text = ""

    div = soup.find('div', {'class': 'mw-parser-output'})

    if div is not None:
        text = div.text

    return text
