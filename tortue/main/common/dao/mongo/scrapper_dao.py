from tortue.main.common.dao.mongo.mongo_cli import MongoCli
from tortue.main.common.model.scrapper.scrapper_meta import ScrapperMeta


class ScrapperDAO:
    def __init__(self):
        self.dao = MongoCli.instance().cli().scrappers

    def save(self, scrapper_meta):
        scrapper_meta.refresh_last_seen()

        self.dao.update(
            {'id': scrapper_meta.id},
            {'id': scrapper_meta.id, 'last_seen': scrapper_meta.last_seen},
            upsert=True
        )

    def find_n_elements(self, n):
        scrappers = []

        for doc in self.dao.find().limit(n):
            if doc['id'] and doc['last_seen']:
                scrapper = ScrapperMeta()
                scrapper.id = doc['id']
                scrapper.last_seen = doc['last_seen']

                scrappers.append(scrapper)

        return scrappers
