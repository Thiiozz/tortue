from tortue.main.scrapper.wiki_scrapper import WikiScrapper

from tortue.main.common.dao.mongo.raw_data_DAO import RawDataDAO
from tortue.main.common.dao.mongo.scrapper_dao import ScrapperDAO

from tortue.main.common.model.scrapper.scrapper_meta import ScrapperMeta
from tortue.main.common.model.data.raw_wiki_data import RawWikiData

from tortue.main.common.utils.logger import LOGGER


class Scrapper:
    def __init__(self):
        self.wiki_scrapper = WikiScrapper()

        self.raw_data_dao = RawDataDAO()
        self.scrapper_dao = ScrapperDAO()

        self.scrapper_meta = ScrapperMeta()

    def run(self):
        while True:
            self.scrap_page_and_save_it()
            self.scrapper_dao.save(self.scrapper_meta)

    def scrap_page_and_save_it(self):
        page_data = self.wiki_scrapper.extract_data_from_random_page()

        if page_data['title'] and page_data['text']:
            LOGGER.info("Persisting doc: %s", page_data['title'])
            self.raw_data_dao.insert(RawWikiData(page_data))
