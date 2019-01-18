# coding: utf8

from pymongo import MongoClient

from tortue.main.common.pattern.Singleton import Singleton
from tortue.main.common.utils.configuration import Configuration


@Singleton
class MongoCli:
    def __init__(self):
        self.client = None
        self.configuration = Configuration.get_instance()

    def cli(self):
        if self.client is None:
            self.client = MongoClient(self.configuration.config()['mongo']['connection_string'])
        return self.client[self.configuration.config()['mongo']['db']]
