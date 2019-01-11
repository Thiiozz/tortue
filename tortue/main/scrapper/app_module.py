# coding utf-8

import inject

from tortue.main.common.utils.configuration import Configuration
from tortue.main.common.dao.mongo.mongo_cli import MongoCli
from tortue.main.common.dao.mongo.raw_data_DAO import RawDataDAO


def inject_dependencies():
    inject.configure(bind)


def bind(binder):
    binder.bind(Configuration, Configuration('./tortue.json'))
    binder.bind(MongoCli, MongoCli())
    binder.bind(RawDataDAO, RawDataDAO())
