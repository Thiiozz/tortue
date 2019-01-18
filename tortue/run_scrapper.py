# coding: utf8

import sys
import time

from tortue.main.scrapper.scrapper import Scrapper
from tortue.main.common.utils.configuration import Configuration

if __name__ == "__main__":
    Configuration.get_instance().load_from_file(sys.argv[1])
    s = Scrapper()

    while True:
        s.scrap_page_and_save_it_to_mongo()
        time.sleep(1)
