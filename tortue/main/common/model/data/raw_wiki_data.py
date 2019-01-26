import time

from tortue.main.common.str.str_cleaner import StrCleaner


class RawWikiData:
    def __init__(self, data):
        self.title = ''
        self.text = ''
        self.status = 'PENDING'
        self.created_at = time.time()

        self.populate(data)

    def populate(self, data):
        if data['title'] and data['text']:
            self.text = StrCleaner.clean(data['text'])
            self.title = StrCleaner.clean(data['title'])

    def to_json(self):
        return '{"title": "%s", "content":"%s"}' % (self.title, self.text[:150])


