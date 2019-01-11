# coding: utf8

import inject
from pymongo import MongoClient
from tortue.main.common.utils.configuration import Configuration


class MongoCli:
    def __init__(self):
        self.configuration = inject.instance(Configuration)
        self.client = None
    
    def cli(self):
        if self.client is None:
            self.client = MongoClient(self.configuration.config()['mongo']['connection_string'])
        return self.client[self.configuration.config()['mongo']['db']]
