import pymongo

from tortue.main.common.dao.mongo.mongo_cli import MongoCli
from tortue.main.common.model.data.raw_wiki_data import RawWikiData


class RawDataDAO:
    def __init__(self):
        self.dao = MongoCli.instance().cli().raw_wiki_data

    def insert(self, doc):
        if doc is not None:
            self.dao.insert_one(
                {'title': doc.title, 'text': doc.text, 'status': doc.status, 'created_at': doc.created_at})

    def find_n_by_status(self, n, status):
        data = []

        for doc in self.dao.find({'status': status}).sort([('created_at', pymongo.DESCENDING)]).limit(int(n)):
            if doc['title'] and doc['text']:
                element = RawWikiData(doc)

                element.created_at = doc['created_at']
                element.status = doc['status']

                data.append(element)

        return data

    def count(self):
        return self.dao.find().count()

    def count_by_status(self, status):
        return self.dao.find({'status': status}).count()
