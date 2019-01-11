# coding: utf8

import inject

from tortue.main.common.dao.mongo.mongo_cli import MongoCli


class RawDataDAO:
    def __init__(self):
        self.cli = inject.instance(MongoCli)

    def insert(self, doc):
        if doc is not None:
            self.cli.cli().raw_wiki_data.insert_one({'title': doc.title, 'text': doc.text})
