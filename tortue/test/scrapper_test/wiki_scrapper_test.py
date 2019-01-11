# coding: utf8

from tortue.main.scrapper.wiki_scrapper import WikiScrapper


def test_can_fetch_a_random_wiki_page():
    s = WikiScrapper()
    assert len(s.get_random_wki_page()) > 0


def test_can_extract_page_title():
    s = WikiScrapper()
    assert len(s.extract_data_from_random_page()['title']) > 1


def test_can_extract_page_text():
    s = WikiScrapper()
    assert len(s.extract_data_from_random_page()['text']) > 1
