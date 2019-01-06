# coding: utf8


from .wiki_scrapper import WikiScrapper
from ..common.dao.mongo.raw_data_DAO import RawDataDAO
from ..common.model.raw_wiki_data import RawWikiData


class Scrapper:
    def __init__(self):
        self.wiki_scrapper = WikiScrapper()
        self.dao = RawDataDAO()

    def scrap_page_and_save_it_to_mongo(self):
        page_data = self.wiki_scrapper.extract_data_from_random_page()
        self.dao.insert(self.transform_to_doc(page_data))

    def transform_to_doc(self, data):
        return RawWikiData(data)

