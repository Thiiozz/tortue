# coding utf-8

import json
import os.path


class Configuration:
    def __init__(self, config_file):
        self.configuration = self.load_from_file(config_file)

    def load_from_file(self, config_file):
        data = {}

        if os.path.isfile(config_file):
            with open(config_file) as f:
                data = json.load(f)

        return data

    def config(self):
        return self.configuration
