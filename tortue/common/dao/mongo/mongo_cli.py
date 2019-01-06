# coding: utf8

from pymongo import MongoClient


class MongoCli:
    def __init__(self):
        self.host = ''
        self.user = ''
        self.password = ''
        self.db = 'tortue'
        self.client = None

    def connection_string(self):
        return 'mongodb://{}:{}@{}'.format(self.user, self.password, self.host)

    def local(self):
        return 'mongodb://localhost:27017/'
    
    def cli(self):
        if self.client is None:
            self.client = MongoClient(self.local())
        return self.client[self.db]
