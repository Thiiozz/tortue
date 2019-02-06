import time

import pandas as pd

from tortue.main.common.utils.logger import LOGGER
from tortue.main.cleaner.french_stop_words import FrenchStopWords
from tortue.main.common.dao.mongo.raw_data_DAO import RawDataDAO
from tortue.main.common.utils.configuration import Configuration


class DataCleaner:
    def __init__(self):
        Configuration.instance().load_from_file('/home/thiiozz/dev/workspace/tortue/tortue.json')
        self.dao = RawDataDAO()
        self.forbidden = ['article', 'articles', 'homonymes' 'ébauche', 'pouvez', 'partager', 'connaissances']

    def run(self):
        while True:
            if self.dao.count_by_status('PENDING') >= 200:
                self.clean_pending_docs()
            else:
                LOGGER.info('waiting more docs')

            time.sleep(5)

    def clean_pending_docs(self):
        LOGGER.info("Start cleaning")
        df = pd.DataFrame.from_records([o.to_dict() for o in self.load_pending_data()])
        df['text'] = df['text'].apply(self.clean_text)
        df['status'] = df['status'].apply(self.update_status)
        df['created_at'] = df['created_at'].apply(self.update_created_at)
        LOGGER.info("Cleaning finnish")

        LOGGER.info("Updating Database")
        for record in df.to_dict('records'):
            self.dao.upsert(record)
        LOGGER.info("Database updated")

    def load_pending_data(self):
        return self.dao.find_n_by_status('PENDING')

    def clean_text(self, words):
        words = set([w for w in words.split(' ') if w not in FrenchStopWords.stop_words() and w not in self.forbidden
                     and 20 > len(w) > 3])

        return str(words)

    def update_status(self, s):
        return 'READY'

    def update_created_at(self, s):
        return time.time()


if __name__ == '__main__':
    DataCleaner().run()
