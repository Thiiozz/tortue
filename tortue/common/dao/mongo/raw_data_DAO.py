# coding: utf8

from ..mongo.mongo_cli import MongoCli


class RawDataDAO:
    def __init__(self):
        self.cli = MongoCli().cli()

    def insert(self, doc):
        if doc is not None:
            self.cli.raw_wiki_data.insert_one({'title': doc.title, 'text': doc.text})
