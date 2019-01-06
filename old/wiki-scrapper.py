# coding: utf8

import requests
import re
from bs4 import BeautifulSoup
import sys

def extract_page_subject(soup):
    output = ""

    h1 = soup.find('h1', {'id': 'firstHeading'})

    if h1 is not None:
        output = h1.text

    return output

def extract_page_text(soup):
    output = ""

    div = soup.find('div', {'class':'mw-parser-output'})

    if div is not None:
        output = div.text

    return output

def format_text(s):
    output = ""

    reg = re.compile('[\w]')

    for line in s.split('\n'):

        if (not 'mw-parser-output' in line and not 'background-image' in line and not 'Vous pouvez partager vos connaissances' in line and not '[' in line and not ']'
            in line and not 'Cet article est une ébauche' in line and not 'Cet article ne cite pas suffisamment ses sources' in line and not 'Portail' in line and not '•' in line):
            line = line.strip()
            line = line.replace(',', ' ')
            line = line.replace(';', ' ')
            line = line.replace('.', ' ')
            line = line[:2000]

            if reg.match(line):
                output += " " + line

    return output

def get_random_wiki_page_dom():
    output = ""

    random_wiki_page_url = 'https://fr.wikipedia.org/wiki/Spécial:Page_au_hasard'
    r = requests.get(random_wiki_page_url)

    if r.status_code == 200:
        output = r.text

    return output

def scrap_data_from(dom):
    output = {}

    soup = BeautifulSoup(dom, 'html.parser')

    subject = extract_page_subject(soup)
    text = format_text(extract_page_text(soup))

    if subject != '' and text != '':
        print('subject: %s' % subject)
        #print('text: %s' % text)
        output = {'subject' : subject, 'text': text}

    return output

def write_data_into_csv(data, csv):
    if data is not None and 'subject' in data and 'text' in data:
        csv.write(data['subject'] + ";" + data['text'] + "\n")

def scrap_n_pages(n):
    csv = open('./dataset.csv', 'a+')

    for i in range(0, n):
        print(str(i) + "/" + str(n))
        try:
            write_data_into_csv(scrap_data_from(get_random_wiki_page_dom()), csv)
        except Exception as e:
            print(e)

    csv.close()

if __name__ == "__main__":
    scrap_n_pages(int(sys.argv[1]))
