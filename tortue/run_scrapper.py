# coding: utf8

import sys

from tortue.main.scrapper.scrapper import Scrapper
from tortue.main.common.utils.configuration import Configuration

if __name__ == "__main__":
    Configuration.instance().load_from_file(sys.argv[1])
    Scrapper().run()
