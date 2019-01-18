# coding utf-8

import json
import os.path

from tortue.main.common.pattern.Singleton import Singleton


@Singleton
class Configuration:
    def __init__(self):
        self.configuration = {}

    def load_from_file(self, config_file):
        data = {}

        if os.path.isfile(config_file):
            with open(config_file) as f:
                self.configuration = json.load(f)
        else:
            raise Exception("%s does not exists !" % config_file)

        return data

    def config(self):
        return self.configuration
